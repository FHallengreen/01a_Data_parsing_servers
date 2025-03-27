
using DataParsingServer;
using Microsoft.AspNetCore.Mvc;

namespace DataParsingAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class DataController : ControllerBase
    {
        private const string BasePath = "../../../datasets/product.";


        [HttpGet("json")]
        public ActionResult<List<Product>> GetJsonData()
        {
            var products = DataParsingService.ParseJson(BasePath + "json");
            return Ok(products);
        }

        [HttpGet("xml")]
        public ActionResult<List<Product>> GetXmlData()
        {
            var products = DataParsingService.ParseXml(BasePath + "xml");
            return Ok(products);
        }

        [HttpGet("yaml")]
        public ActionResult<List<Product>> GetYamlData()
        {
            var products = DataParsingService.ParseYaml(BasePath + "yaml");
            return Ok(products);
        }

        [HttpGet("csv")]
        public ActionResult<List<Product>> GetCsvData()
        {
            var products = DataParsingService.ParseCsv(BasePath + "csv");
            return Ok(products);
        }

        [HttpGet("text")]
        public ActionResult<List<Product>> GetTextData()
        {
            var products = DataParsingService.ParseText(BasePath + "txt");
            return Ok(products);
        }
    }
}
