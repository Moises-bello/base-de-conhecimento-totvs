---
content_hash: f6387b92cbde24ddb13a2d35b3fe3d0def99b98acfb985afa1b0a0653975d689
fetched_at: '2026-06-29T00:10:53.162356+00:00'
page_id: '577610090'
product: rm
source: tdn-rm
title: Coleta de informações de uso do portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=577610090
version: 8
---

No novo portal do aluno é possível configurar o serviço do Google Analytics.

Google Analytics é um serviço oferecido pela Google que expõe, entre outras coisas, estatísticas sobre o tráfego do site configurado.

Para realizar a configuração será necessário criar uma conta conforme o link abaixo: <https://analytics.google.com/analytics/web/>

A criação da conta é simples e basta seguir os três passos conforme abaixo.

No momento da criação da conta é importante informar algumas informações, acessar o caminho: Google Analytisc | Administrador | Fluxo de Dados | Selecionar o Fluxo de Dados: Web

**Nome do Proprietário –** Nome que será utilizado na criação da conta do Google Analytics onde serão controlado as informações do site.

**URL Padrão –** URL pública utilizada pelo novo Portal do Aluno.

**Ex:** [http://DOMINIO:PORTA/WEB/APP/EDU/PORTALEDUCACIONAL/](http://DOMINIOPORTA)

Finalizando o processo de criação da conta será gerado uma chave (ID da Métrica). Esta chave que será utilizada para coletar as informações.

Atenção

O código acima 'G-BLLW6D3R7M' é único e deve ser utilizado o que foi gerado para a conta criada.

Para iniciar o controle das informações do Google Analytics, basta copiar o ID da Métrica gerado, no exemplo acima, G-BLLW6D3R7M e inserir o mesmo na variável EDU\_CONST\_GOOGLE\_ANALYTICS que se encontra no arquivo edu-contantes.global.config.js, disponível no caminho padrão do instalador do novo Portal do Aluno. “C:\totvs\CorporeRM\FrameHTML\Web\App\Edu\PortalEducacional\js”.

Atenção

Caso a variável EDU\_CONST\_GOOGLE\_ANALYTICS não se encontre no arquivo  edu-contantes.global.config.js, basta incluí-la.

Observação

Todas as páginas acessadas pelo aluno no portal são registradas como visualização pelo analytcs. O campo user\_id do analytcs é preenchido com o código do usuário logado.
