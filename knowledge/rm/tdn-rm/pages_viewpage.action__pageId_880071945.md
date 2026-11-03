---
content_hash: 414353650648d7790e73a744c471d26f259be70deb5d67378473f28fd3611f89
fetched_at: '2026-06-29T00:12:00.143439+00:00'
page_id: '880071945'
product: rm
source: tdn-rm
title: Como fazer uma nova atualização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=880071945
version: 13
---

Este documento apresenta um guia passo a passo para realizar a atualização do **TOTVS Automação de Testes**.

1Onde baixar?;Como instalar?

Caso haja alguma dúvida ou seja necessário aprofundar a análise para atualização do TOTVS Automação, recomenda-se consultar a documentação de Implantação, onde estão descritos os procedimentos e pré-requisitos detalhados.

Caso haja dúvidas ou seja necessário aprofundar a análise do processo, recomenda-se consultar também a documentação de **Implantação**, onde estão descritos os procedimentos completos e os pré-requisitos do ambiente.

#21cafcdashedDownload e Execução

Antes de iniciar a atualização, realize as seguintes verificações:

**Backup:** Recomendamos realizar um backup preventivo da base de dados e do arquivo `appsettings.json`.

**Frameworks:** Verifique se a nova versão exige a instalação ou inclusão de novos Frameworks.

* **.NET Core 2.2 – Hosting Bundle**  
  Necessário para execução de aplicações web hospedadas no servidor (inclui suporte ao IIS e runtime do .NET).  
  Download:  
  [Baixar .NET Core 2.2 Hosting Bundle](https://dotnet.microsoft.com/pt-br/download/dotnet/2.2?utm_source=chatgpt.com)
* **.NET 8 – Runtime**  
  Necessário para execução das aplicações que utilizam essa versão da plataforma .NET.  
  Download:  
  [Baixar .NET 8 Runtime](https://dotnet.microsoft.com/pt-br/download/dotnet/8.0?utm_source=chatgpt.com)

**Download:** Obtenha a versão mais recente: <https://testflowstorage.blob.core.windows.net/latest/TOTVSAutomacao.exe>

#21cafcdashed2. Fluxo de Atualização no Instalador

Para garantir que a atualização seja bem-sucedida, execute o arquivo como **Administrador** e siga estas etapas:

**Seleção de Componentes:**  
Durante a atualização, selecione apenas os componentes necessários no instalador.

* Para processos de **atualização**, mantenha **somente a opção “Aplicação Principal” selecionada**, que corresponde aos arquivos binários, front-end e serviços do Website (Host).
* A opção **“Base Vazia”** deve permanecer **desmarcada**, pois ela é utilizada apenas quando se deseja que o instalador **disponibilize ou gere o arquivo de backup (.bak)** para criação de uma nova base posteriormente no SQL Server.
#21cafcdashed3. Configurações Pós-Atualização

Após o término do instalador, realize as seguintes validações:

* **Parar o IIS:** Antes de iniciar a atualização, é necessário **parar o Site no IIS** para evitar conflitos durante a substituição dos arquivos da aplicação. No **Gerenciador do IIS**, localize o site correspondente ao **TOTVS Automação de Testes** e selecione a opção **Stop (Parar)**. Após parar o site, execute o instalador normalmente para realizar a atualização.
* **Validação do appsettings.json:** Em atualizações maiores, o formato do JSON ou novas chaves podem ser necessários. Compare seu arquivo atual com os requisitos da nova versão.
* **Verificação do Endpoint:** Certifique-se de que a porta configurada no IIS e a tag `"Endpoint"` no JSON continuam consistentes.
* **Reinicialização do IIS:** É recomendável realizar um *Restart* no Site através do Gerenciador do IIS para garantir que o novo código seja carregado corretamente.

 Se o sistema apresentar erro após a atualização, navegue até a pasta do Host via CMD e execute `dotnet ./TestFlow.Host.dll`. Isso revelará se há alguma dependência de framework ausente ou erro de conexão com o banco.

# Utilizando o instalador

Atualização com instalador

**1.**

**2.**

**3.**

**4.**

**5.**

**6.**

# Resultado

Após a execução dos passos o TOTVS Automação de Testes já estará disponível.
