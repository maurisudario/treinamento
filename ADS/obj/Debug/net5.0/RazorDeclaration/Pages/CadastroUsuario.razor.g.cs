// <auto-generated/>
#pragma warning disable 1591
#pragma warning disable 0414
#pragma warning disable 0649
#pragma warning disable 0169

namespace ProjetoBlazor.Pages
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Components;
#nullable restore
#line 1 "D:\Uniceub\2021\ADS\_Imports.razor"
using System.Net.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.AspNetCore.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.AspNetCore.Components.Authorization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.AspNetCore.Components.Forms;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.AspNetCore.Components.Routing;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.AspNetCore.Components.Web;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.AspNetCore.Components.Web.Virtualization;

#line default
#line hidden
#nullable disable
#nullable restore
#line 8 "D:\Uniceub\2021\ADS\_Imports.razor"
using Microsoft.JSInterop;

#line default
#line hidden
#nullable disable
#nullable restore
#line 9 "D:\Uniceub\2021\ADS\_Imports.razor"
using ProjetoBlazor;

#line default
#line hidden
#nullable disable
#nullable restore
#line 10 "D:\Uniceub\2021\ADS\_Imports.razor"
using ProjetoBlazor.Shared;

#line default
#line hidden
#nullable disable
    [Microsoft.AspNetCore.Components.RouteAttribute("/CadastroUsuario")]
    public partial class CadastroUsuario : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
        }
        #pragma warning restore 1998
#nullable restore
#line 114 "D:\Uniceub\2021\ADS\Pages\CadastroUsuario.razor"
 
    public string MostrarMensam = "none";
    public Usuario usuario = new Usuario();

    public IList<Usuario> TodosUsuarios = new List<Usuario>();

    protected override async Task OnInitializedAsync()//Quando Inicia a página
    {
        CarregarUsuarios();
    }

    public void CarregarUsuarios()
    {
        TodosUsuarios = new UsuarioDAO().BuscarUsuarios();
    }
    async Task ExcluirUsuario(Usuario usuario)
    {
        new UsuarioDAO().ExcluirUsuario(usuario);
        //JS.InvokeAsync<string>("ShowTab", "tabForm");
        CarregarUsuarios();
    }

    async Task AlterarUsuario(Usuario _usuario)
    {
        usuario = _usuario;
        JS.InvokeAsync<string>("ShowTab", "tabForm");
    }

    public void GravarUsuario()
    {
        usuario.USUDATAHORACRIACAO = DateTime.Now;
        if(string.IsNullOrEmpty(usuario.USULOGIN) || 
           string.IsNullOrEmpty(usuario.USUEMAIL) ||
           string.IsNullOrEmpty(usuario.USUNOMECOMPLETO)||
           string.IsNullOrEmpty(usuario.USUSENHA))
        {
            MostrarMensam = "block";
        }else
        {
            if(usuario.USUID>0)
            {
                //Isso é uma alteração
                new UsuarioDAO().AtualizarUsuario(usuario);
            }
            else
            {
                new UsuarioDAO().InserirUsuario(usuario);
            }

            CarregarUsuarios();
            usuario = new Usuario();
            JS.InvokeAsync<string>("ShowTab", "tabLista");
        }
    }

    public void CancelarAcao()
    {
        usuario = new Usuario();
        JS.InvokeAsync<string>("ShowTab", "tabLista");
    }

#line default
#line hidden
#nullable disable
        [global::Microsoft.AspNetCore.Components.InjectAttribute] private IJSRuntime JS { get; set; }
    }
}
#pragma warning restore 1591
