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
    public class UsuarioDAO
    {
        string Conexao01 = @"Server=LENOVO_EDES\SQLEXPRESS;Database=dbsistec;User Id=usrceub;Password=123456;MultipleActiveResultSets=True";

        string ConexaoMyql = "Server=localhost;Database=test;Uid=usuario;Pwd=senha";

        public UsuarioDAO()
        {

        }

        ///CRUD
        public void InserirUsuario(Usuario usuario)
        {
            /*using (MySql.Data.MySqlClient.MySqlConnection conn = new MySql.Data.MySqlClient.MySqlConnection(ConexaoMyql))
            {
                conn.Open();
                conn.Insert<Usuario>(usuario);
            }*/
            //Conectar ao Banco de Dados e dar um insert
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                conn.Insert<Usuario>(usuario);
            }
        }

        public void AtualizarUsuario(Usuario usuario)
        {
            //Conectar ao Banco de Dados e dar um insert
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                conn.Update<Usuario>(usuario);
            }
        }

        public void ExcluirUsuario(Usuario usuario)
        {
          using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                conn.Delete<Usuario>(usuario);
            }  
        }

        public Usuario BuscarUsuario(int UsuarioId)
        {
            //string sql = "Select * from TB_Usuario Where USUID=@USUID";
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                return conn.Get<Usuario>(UsuarioId);
                //return conn.Query<Usuario>(sql,new{USUID=UsuarioId}).FirstOrDefault();
            } 
        }

        public Usuario BuscarUsuarioByLogin(string Login, string Senha)
        {
            string sql = "Select * from TB_Usuario Where USULOGIN=@USULOGIN And USUSENHA=@USUSENHA";
            
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                return conn.Query<Usuario>(sql,new{USULOGIN=Login,USUSENHA=Senha}).FirstOrDefault();
            } 
        }

        public IList<Usuario> BuscarUsuarios()
        {
            //string sql = "Select * from TB_Usuario";
            using (System.Data.SqlClient.SqlConnection conn = new System.Data.SqlClient.SqlConnection(Conexao01))
            {
                conn.Open();
                return conn.GetAll<Usuario>().ToList();
                //return conn.Query<Usuario>(sql).ToList();
            } 
        }

    }
}
