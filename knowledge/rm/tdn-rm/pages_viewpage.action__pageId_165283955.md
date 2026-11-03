---
content_hash: 273dd1e822cbef7ea006c242328011624374e59977a0c486e184303bc498a4f8
fetched_at: '2026-06-29T00:05:57.230502+00:00'
page_id: '165283955'
product: rm
source: tdn-rm
title: Geração CAGED de acordo com Portaria 1.129
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=165283955
version: 2
---

Produto

**RMLabore**

**Processo:** **Geração CAGED de acordo com Portaria 1.129**

**Versão: 11.82 - 11.82.35.139(biblioteca específica) ou superior**

**11.52 - 11.52.63(7) (aplicativo específico) ou superior**

Atenção

Para versão 11.52 será gerado apenas Caged em Delphi. Caso queira gerar através do menu (Relatório | Caged (.NET)) utilizar o link abaixo.

<http://tdn.totvs.com.br/pages/releaseview.action?pageId=161350629>

No cadastro de funcionários foi incluído o campo **“Estava recebendo seguro desemprego na admissão”** para informar se o funcionário admitido estava recebendo o seguro desemprego na data de admissão

Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)

### **Geração do CAGED**

**1 -** Foi incluído na geração do CAGED, a opção para o usuário informar se deseja a geração do arquivo diário ou mensal

Tela Delphi (Clique para visualizar imagem)Tela .Net (Clique para visualizar imagem)

**a.** Para a geração do CAGED diário, o usuário deverá selecionar a opção “Diário” e informar a data de admissão a ser considerada no CAGED. O sistema gerará arquivo considerando os funcionários com admissão na data informada e que estejam com o campo “Estava recebendo seguro desemprego na admissão” marcado.

**b.** Para a geração do CAGED mensal, o usuário deverá selecionar a opção “Mensal”. O sistema gerará arquivo considerando os funcionários com admissão na competência informada e que estejam com o campo “Estava recebendo seguro desemprego na admissão” desmarcado, além dos funcionários com data de demissão na competência.
