using System;
using Dapper.Contrib;
using Dapper.Contrib.Extensions;

namespace ProjetoBlazor
{
    //ORM
   [Table("TB_USUARIO")]
    public class Fornecedor
    {
        [Key]
        public int FORNID {get;set;}
        public string FORNLOGIN {get;set;}
        public string FORNEMAIL {get;set;}
        public string FORNEMPRESA {get;set;}
        public string FORNSENHA {get;set;}
        public DateTime FORNDATAHORACRIACAO {get;set;}
        public bool FORNATIVO {get;set;}
        public string FORNCNPJ {get;set;}
        public string FORNTELEFONE {get;set;}
    }
}