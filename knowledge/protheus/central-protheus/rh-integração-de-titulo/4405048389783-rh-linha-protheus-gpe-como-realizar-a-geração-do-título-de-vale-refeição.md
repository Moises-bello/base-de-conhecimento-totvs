---
article_id: 4405048389783
category: RH - Integração de Titulo
content_hash: 53621abce9e16e02401d4fdfa1d074a64035a1347bb659f9ce0b0cf439f574d6
fetched_at: '2026-06-28T22:43:36.280820+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a geração do título de Vale Refeição
type: support-article
updated_at: '2025-07-18T14:09:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405048389783-RH-Linha-Protheus-GPE-Como-realizar-a-gera%C3%A7%C3%A3o-do-t%C3%ADtulo-de-Vale-Refei%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558825144215)Tempo aproximado para leitura: 00:03:00 min

**Dúvida**Como gerar um título de Vale Refeição?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Realize o cálculo do **Roteiro VRF**, integre a folha e processe o cálculo do roteiro **FOL**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041557911)  
![Integra__o_Roteiro.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/33558825147287)  
  
2. Acesse **Miscelânea -> Títulos -> Definição** e configure um título de Vale Refeição. No exemplo abaixo usaremos o **Agrupamento** por filial (gerando 1 título para cada filial).   
Após as configurações iniciais, selecione **Definir título**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041630231)  
  
3. Será apresentada uma janela para selecionarmos a verba e a tabela onde buscaremos o cálculo para geração do título. **Tratando-se de verbas da folha de pagamento, o cálculo estará na tabela SRC, estando o respectivo mês com período fechado os dados devem ser buscados na SRD**e utilizaremos como filtro para busca a Data de Referência.  
A tabela para busca de dados do título deve obrigatoriamente conter os campos **Filial**, **Centro de Custo**, **Verba** e **Valor**, sendo assim não é possível selecionar as tabelas **SR0 - Itens de Benefícios** ou **RG2 - Histórico de Benefícios** para geração.  
**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405048132247)  
Atenção:** A verba selecionada deverá possuir a legenda verde para que seja considerada como positiva, no exemplo acima foram utilizadas as verbas com **identificadores de cálculo 0050 - Vale Refeição** e **0212 - Base parte Empresa V. Refeição**.  
  
4. Acesse **Miscelânea ->Títulos -> Geração** e configure os parâmetros de acordo com o título que será gerado:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041838359)  
  
5. Acesse **Miscelânea -> Títulos -> Manutenção** e verifique as informações do título gerado. O valor do título será a somatória das verbas selecionadas na definição do título:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405041904791)  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
