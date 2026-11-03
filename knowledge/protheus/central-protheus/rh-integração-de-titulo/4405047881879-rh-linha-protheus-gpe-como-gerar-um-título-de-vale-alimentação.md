---
article_id: 4405047881879
category: RH - Integração de Titulo
content_hash: 41c117a07cab84a654d0d3bdf4a431fabdb37584318b44f70f7ad97bef42a328
fetched_at: '2026-06-28T22:43:36.255987+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar um título de Vale Alimentação
type: support-article
updated_at: '2025-07-21T20:22:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405047881879-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-Vale-Alimenta%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33616895697303)** Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Como gerar um título de Vale Alimentação?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões.

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Realize o cálculo do Roteiro **VAL**, integre a folha e processe o cálculo do roteiro **FOL**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405047142679)  
![Integra__o_Roteiro.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/33616895702295)  
  
2. Acesse **Miscelânea -> Títulos -> Definição** e configure um título de Vale Alimentação. No exemplo abaixo usaremos o **Agrupamento** por filial (gerando 1 título para cada filial).   
Após as configurações iniciais, selecione **Definir título**.![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041084055)  
  
3. Será apresentada uma janela para selecionarmos a verba e a tabela onde buscaremos o cálculo para geração do título. **Tratando-se de verbas da folha de pagamento, o cálculo estará na tabela SRC, estando o respectivo mês com período fechado os dados devem ser buscados na SRD**e utilizaremos como filtro para busca a Data de Referência.  
A tabela para busca de dados do título deve obrigatoriamente conter os campos **Filial**, **Centro de Custo**, **Verba** e **Valor**, sendo assim não é possível selecionar as tabelas **SR0 - Itens de Benefícios**ou **RG2 - Histórico de Benefícios** para geração.  
**![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041247639)  
Atenção:** A verba selecionada deverá possuir a legenda verde para que seja considerada como positiva.  
  
4. Acesse **Miscelânea ->Títulos -> Geração** e configure os parâmetros de acordo com o título que será gerado.  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041301015)  
  
5. **Acesse Miscelânea -> Títulos -> Manutenção** e verifique as informações do título gerado. O valor do título será a somatória das verbas selecionadas na definição do título.

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405047786135)  
  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
