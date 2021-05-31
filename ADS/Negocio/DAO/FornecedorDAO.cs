using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Dapper;
using Dapper.Contrib;
using Dapper.Contrib.Extensions;
using System.Data.SqlClient;

namespace ProjetoBlazor
{
    public class FornecedorDAO
    {
        string Conexao01 = @"Server=LENOVO_EDES\SQLEXPRESS;Database=dbsistec;User Id=usrceub;Password=123456;MultipleActiveResultSets=True";
        string Conexao02 = @"Data Source=LENOVO_EDES\SQLEXPRESS;Initial Catalog=dbsistec;User Id=usrceub;Password=123456;MultipleActiveResultSets=True";

        public FornecedorDAO()
        {

        }

        ///CRUD
        public void InserirFornecedor(Fornecedor fornecedor)
        {
            //Conectar ao Banco de Dados e dar um insert
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                conn.Insert<Fornecedor>(fornecedor);
            }
        }

        public void AtualizarFornecedor(Fornecedor fornecedor)
        {
            //Conectar ao Banco de Dados e dar um insert
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                conn.Update<Fornecedor>(fornecedor);
            }
        }

        public void ExcluirFornecedor(Fornecedor fornecedor)
        {
          using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                conn.Delete<Fornecedor>(fornecedor);
            }  
        }

        public Usuario BuscarFornecedor(int FornecedorId)
        {
            //string sql = "Select * from TB_Fornecedor Where FORNID=@FORNID";
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                return conn.Get<Fornecedor>(FornecedorId);
                //return conn.Query<Fornecedor>(sql,new{FORNID=FornecedorId}).FirstOrDefault();
            } 
        }

        public IList<Fornecedor> BuscarFornecedor()
        {
            //string sql = "Select * from TB_Fornecedor";
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                return conn.GetAll<Fornecedor>().ToList();
                //return conn.Query<Fornecedor>(sql).ToList();
            } 
        }

    }
}
