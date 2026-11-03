---
article_id: 360020775191
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 5f981120dc089118a297fddb0892513568eb514103ab4ea0976305ded95b8768
fetched_at: '2026-06-28T22:37:56.412240+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - O que analisar quando
  Retorno CNAB não baixa título
type: support-article
updated_at: '2025-04-25T20:23:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020775191-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-O-que-analisar-quando-Retorno-CNAB-n%C3%A3o-baixa-t%C3%ADtulo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00min**

**Dúvida**O que analisar quando Retorno CNAB não baixa título?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir versão 11.8  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:

1. Verifique qual o código da ocorrência que o banco está enviando no **arquivo de retorno**;  
2. Acesse o Manual do banco ou o arquivo de configuração e verifique o código da ocorrência. Caso seja ocorrência: **Entrada Confirmada**, não irá baixar os títulos, pois esta ocorrência é apenas uma informação do banco avisando que o título foi processado;  
3. Caso seja ocorrência do código 00 ou 06 o título deve ser baixado. **Acesse Relatório > Comunicação Bancária > Relatório de Retorno CNAB** informe nas perguntas dos **parâmetros** deste relatório o diretório que está salvo arquivo que deseja processar e o arquivo de configuração. Enquanto o relatório não gerar com as informações que constam no arquivo de retorno os títulos não serão baixados. Este relatório apresentando em branco ou gerando como: "Arquivo Vazio" é devido alguma falha na estrutura do arquivo de configuração. Neste caso acesse: **Atualizações > Cadastro > Parâmetros Bancos** e acesse o cadastro correspondente o banco utilizado no retorno. Verifique o conteúdo do campo: **Nro. *Bytes***, pois deve estar preenchido com o valor de acordo com a estrutura do seu arquivo de retorno. Exemplo, este campo deve estar 400 caso trabalhe com modelo 1, ou 240 caso trabalhe com modelo 2.  
4. Acesse cadastro: **Parâmetros Bancos**, verifique o conteúdo do campo: **Extensão(EE\_EXTEN).** O conteúdo deste campo deve estar de acordo com a extensão do arquivo de retorno.   
Segue exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040859634/mceclip0.png)

**Importante:**Caso o problema persiste de não baixar o título, verificar se o seu ambiente está atualizado conforme o pacote acumulado do financeiro.
