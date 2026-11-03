---
content_hash: 088d4df04aa8604ef86c179ded6d67d2ff4c7db883f197e1dbc11a53309662e0
fetched_at: '2026-06-29T00:11:46.483124+00:00'
page_id: '822687738'
product: rm
source: tdn-rm
title: serv/obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=822687738
version: 13
---

Obs.: O Grupo endereço da Obra "end" será gerado apenas quando o campo "cObra" não for gerado.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Pai | Obrigatório | Origem | Descrição |
| **obra** | **DPS/infDPS/serv** | **Não** |  | **Grupo de informações relativas à obra de construção civil e congêneres.** |
| inscImobFisc | **DPS/infDPS/serv/obra** | Não | MPRJCOMPL.INSCMUNOBRA  Criar o campo complementar no projeto com o nome INSCMUNOBRA, o tamanho e tipo do campo deve ser verificado no manual da NFS-e Nacional | Inscrição imobiliária fiscal (código fornecido pela prefeitura para a identificação da obra ou para fins de recolhimento do IPTU). |
| cObra | **DPS/infDPS/prest/serv/obra** | Não | MPRJ.CGC | Número de identificação da obra. Cadastro Nacional de Obras (CNO) ou Cadastro Específico do INSS (CEI).  **1. Regra para Rio de Janeiro (Capital)** A tag é preenchida seguindo esta ordem de prioridade:  **CEI**: Se houver um CEI válido.  **Campo Complementar**: Se o CEI for inválido/vazio, busca o valor do campo complementar CODOBRAPREF.  **Código do Projeto**: Se o código do projeto estiver preenchido com valor diferente de "COI", preenche com: "CO" + Código do Projeto.  **2. Regra para Demais Municípios** **Regra padrão**: Utiliza o CNPJ do Projeto.  **Caso não possua CEI válido**: Utiliza o campo complementar CODOBRAPREFOUTROS. Configuração de Campos Complementares Para que as regras acima funcionem, os campos devem ser criados em:  Construção | Obras e Projetos > Cad. Gerais > Campos Complementares > Projeto   |  |  |  |  | | --- | --- | --- | --- | | **Nome da Coluna** | **Tipo** | **Subtipo** | **Uso** | | **CODOBRAPREF** | Alfanumérico | Texto | RJ (quando não há CEI) | | **CODOBRAPREFOUTROS** | Alfanumérico | Texto | Outras Cidades (quando não há CEI) | |
| cCIB | **DPS/infDPS/serv/obra** | Não | MPRJ.CIB | Código do Cadastro Imobiliário Brasileiro - CIB |
| end | **DPS/infDPS/serv/obra** | Não | Endereço da Obra | **[Grupo de informações do endereço da obra.](https://tdn.totvs.com/pages/viewpage.action?pageId=822687782)** |

Os campos **`cCIB`**, **`cObra`** e **`end`** são mutuamente exclusivos. A geração segue a seguinte prioridade:

1. **`cCIB`**: quando informado, é gerado com prioridade máxima.
2. **`cObra`**: gerado somente se o `cCIB` não estiver informado.
3. **`end`** : gerado apenas quando `cCIB` e `cObra` não estiverem informados.
