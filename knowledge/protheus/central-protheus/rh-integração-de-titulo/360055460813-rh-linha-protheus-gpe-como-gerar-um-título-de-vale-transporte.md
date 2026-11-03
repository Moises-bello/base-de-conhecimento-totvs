---
article_id: 360055460813
category: RH - Integração de Titulo
content_hash: 8b08b7228454e7f1b51895a33f7928080f7cbb99ebd4f32dc02b054e0b9703f9
fetched_at: '2026-06-28T22:43:36.260454+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Como gerar um título de Vale Transporte
type: support-article
updated_at: '2025-07-21T20:22:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055460813-RH-Linha-Protheus-GPE-Como-gerar-um-t%C3%ADtulo-de-Vale-Transporte
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33616891888663)** Tempo aproximado para leitura: **00:02:30 min**

**Dúvida**Como gerar um título de Vale Transporte?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões.

**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Realize o cálculo do **Roteiro VTR**, integre a folha e processe o cálculo do roteiro **FOL**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405048559639)  
![Integra__o_Roteiro.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360091986893)  
  
2. Acesse **Miscelânea -> Títulos -> Definição** e configure um título de Vale Transporte. No exemplo abaixo usaremos o **Agrupamento** por filial (gerando 1 título para cada filial).   
Após as configurações iniciais, selecione **Definir título**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405042177815)  
  
3. Será apresentada uma janela para selecionarmos a verba e a tabela onde buscaremos o cálculo para geração do título. **Tratando-se de verbas da folha de pagamento, o cálculo estará na tabela SRC, estando o respectivo mês com período fechado os dados devem ser buscados na SRD**e utilizaremos como filtro para busca a Data de Referência.  
A tabela para busca de dados do título deve obrigatoriamente conter os campos **Filial**, **Centro de Custo**, **Verba** e **Valor**, sendo assim não é possível selecionar as tabelas **SR0 - Itens de Benefícios** ou **RG2 - Histórico de Benefícios** para geração.  
**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405048610839)  
Atenção:** A verba selecionada deverá possuir a legenda verde para que seja considerada como positiva, no exemplo acima foram utilizadas as verbas com os Identificadores de cálculo **0050 - Vale Transporte Desconto** e **00210 - Base parte Empresa V. Transporte**.  
  
4. Acesse **Miscelânea ->Títulos -> Geração** e configure os parâmetros de acordo com o título que será gerado:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405042284183)  
  
5. Acesse **Miscelânea -> Títulos -> Manutenção** e verifique as informações do título gerado. O valor do título será a somatória das verbas selecionadas na definição do título:![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405042293015)  
  
**Saiba Mais**  
[Artigos sobre Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
