---
article_id: 1500008543601
category: RH - Integração de Titulo
content_hash: 836aff8d561e88b00435f54c0c2a1ed2684b3d93e26b5628d07572207b470ea7
fetched_at: '2026-06-28T22:43:36.220599+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como criar e configurar um título para Pagamento
  de Autônomo
type: support-article
updated_at: '2025-07-23T12:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008543601-RH-Linha-Protheus-GPE-Como-criar-e-configurar-um-t%C3%ADtulo-para-Pagamento-de-Aut%C3%B4nomo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33657778502551)Tempo aproximado para leitura:00:03:00 min**

**Dúvida**Como criar e configurar um título para Pagamento de Autônomo  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1) Acesse **Miscelânea** -> **Títulos** -> **Definição - GPEM640**:  
  
2) Preencha os campos da rotina Definição de título:  
**Atenção:** os campos preenchidos no exemplo abaixo são meramente ilustrativos.   
![](https://totvssuporte.zendesk.com/attachments/token/3Dybbp4bJWgNbuP4Bo1ok1UWu/?name=inline-368522221.png)  
Para que seja gerado **1 título para cada um dos Autônomos** será necessário que os procedimentos de **Cadastramento Automático de Fornecedores com as informações de Funcionários** tenham sido executados, no final do artigo no tópico **Saiba Mais,** possui o(s) *link*(s) de outras documentações com as instruções deste processo.  
  
3) No canto inferior direito, clique em "**Definir título**" para selecionar a verba e a tabela para busca da informação;  
  
4)  Na definição de título, especifique a verba para geração (**Identificador de Cálculo - ID 0047**) e a tabela para busca dos valores. No exemplo abaixo, apresentamos a verba de ID 0047 e a busca na **tabela SRD - Acumulado,** uma vez que o roteiro AUT foi fechado:  
![](https://totvssuporte.zendesk.com/attachments/token/GLCsC9SrZfS2or1EbDfhH99pN/?name=inline-1653496720.png)

5) Os roteiros **FOL** e **AUT** utilizam o mesmo Identificador de Cálculo (0047) para geração de líquidos, desta forma será necessário criar um filtro nas definições de regras, barrando a geração por Categoria.  
Clique no botão de filtro para que a janela de expressão seja aberta e inclua o seguinte conteúdo:   
  
**"Categoria funcionário IGUAL de A"**  
**![](https://totvssuporte.zendesk.com/attachments/token/jfw7ODODRwEBFaigDgrChHV3A/?name=inline225869679.png)**

6) Acesse **Miscelânea** -> **Títulos** -> **Geração - GPEM650:** configurando os campos de acordo com a definição de título e datas de geração.  
  
7) Verifique na rotina Manutenção se o título gerado foi gerado corretamente  
Acesse: **Miscelânea** -> **Títulos** -> **Manutenção** **- GPEM660**:  
![](https://totvssuporte.zendesk.com/attachments/token/4hf1RhJzCo2i3zIgbIKdBKRWK/?name=inline2019130865.png)  
  
O título será gerado com o **código de** **Fornecedor** processado para o Autônomo:  
![](https://totvssuporte.zendesk.com/attachments/token/Zio5364d3lT4APWDp5TpnnD5j/?name=inline-2029409389.png)  
  
8) Você pode confrontar os valores gerados com o Relatório da Folha de Pagamento - GPER040/GPER106  
Acesse: **Relatórios** -> **Periódicos** -> **Folha de Pagamento**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012477222)

Você também pode utilizar o Recibo de Pagamento Autônomo - IMPRPA  
Acesse: **Relatórios** -> **Recibos** -> **Recibo Autônomo**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500012477042)  
Para que seja possível imprimir o RPA, o *rdmake* **IMPRPA** **deve ser compilado** no seu repositório, este fonte esta contido na pasta ***Rdmakes*** do **Pacote de Expedição Contínua do RH**.

**Saiba Mais**  
[MP - GPE - Cadastro Automático de Fornecedores com as informações de Funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015466272-MP-GPE-Cadastro-Autom%C3%A1tico-de-Fornecedores-com-as-informa%C3%A7%C3%B5es-de-Funcion%C3%A1rios?source=search)  
[MP - GPE - Como configurar o parâmetro MV\_AUTPART](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052083833-MP-GPE-Como-configurar-o-par%C3%A2metro-MV-AUTPART?source=search)  
[RH - Linha Protheus - APD - Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051031874-RH-Linha-Protheus-APD-Como-relacionar-os-Participantes?source=search)
