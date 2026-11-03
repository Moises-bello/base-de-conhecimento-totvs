---
article_id: 14916454178199
category: Financeiro
content_hash: 148b8de21c71ec12613f5156872488612835adefebdaf79a91423e8d35234c96
fetched_at: '2026-06-28T22:38:03.195404+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA918 - HELP: F918GVBCO'
type: support-article
updated_at: '2025-05-21T13:46:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14916454178199-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA918-HELP-F918GVBCO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15884930558743) Tempo aproximado para leitura: **00:10:00min****Ocorrência**No módulo Financeiro , ao tentar realizar a Conciliação de pagamentos( FINA918) , apresenta a mensagem HELP F918GVBCO   
Problema: Banco/Conta não cadastrada. Verificar o Cadastro de Bancos

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14916372834071)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.33  
  
**Causa**Esse incidente ocorre, pois o banco informado na tabela FIF que foi importado pela rotina FINA914 - Importação, não existe.   
**Campos: FIF\_CODBCO, FIF\_CODAGE, FIF\_NUMCC** não batem com o **A6\_COD, A6\_AGENCIA, A6\_NUMCON (Cadastros de Bancos)**  
  
Em muitas ocasiões, os dados gravados pela importação adicionam zeros a esquerda ou a direita e como a rotina faz a comparação se o valor é igual, gera o HELP  
  
**Solução**

Necessário avaliar o conteúdo dos campos da **FIF** abaixo e cadastrar o banco informado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14917084650647)  
**FIF\_CODBCO**  
**FIF\_CODAGE**  
**FIF\_NUMCC  
  
Voce pode entrar em contato com a Administradora de Cartão ou equipe Responsavel pela homologação da conciliação e retalar o ocorrido para ajuste ou orientação no site da administradora para o download correto das informções**

**Importante**  
Lembrando que a tabela **FIF** é alimentado com informação do arquivo, então, caso estiver errado a informação nesse campo, deverá validar no arquivo  
  
**Caso não seja possivel alterar a informação dentro do arquivo, se faz necessário parametrizar o ponto de entrada abaixo para ajustar a conta de baixa dos titulos**

O ajuste pode ser feito na gravação dos dados bancários nas tabelas SE1 (Títulos a Receber) e SE5 (Movimento Bancário) pelo Ponto de Entrada:   
[FINA910F - Define os dados bancários utilizados na baixa](https://tdn.totvs.com/pages/viewpage.action?pageId=6071647)

**Saiba mais**  
[Conciliador Pagamentos e Vendas - Financeiro (Contas a Receber) - P12](https://tdn.totvs.com/display/public/PROT/Conciliador+Pagamentos+e+Vendas+-+Financeiro+%28Contas+a+Receber%29+-+P12)  
[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)
