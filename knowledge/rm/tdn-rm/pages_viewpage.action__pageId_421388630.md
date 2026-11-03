---
content_hash: c46c650bddbd92b8ac517fb9c9a700ad987af185f1c592c97c08988a00a33754
fetched_at: '2026-06-29T00:09:17.722991+00:00'
page_id: '421388630'
product: rm
source: tdn-rm
title: Gerando um arquivo de remessa de Cobrança Eletrônica 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388630
version: 4
---

Para gerar a remessa é necessário que o usuário tenha permissão de acesso ao Segmento Integração. É necessário também que o layout do relatório esteja disponível no segmento Integração/Gerador de Saídas. Este layout deverá ser informado como default no cadastro do Convênio, aba Remessa Bancária, para a Cobrança Eletrônica e/ou para Cobrança Eletrônica PIX.   
A geração do arquivo de remessa de Cobrança Eletrônica e/ou Cobrança Eletrônica PIX será pelo menu de Contas a Pagar / Receber / Boletos. Inicialmente será necessário criar um filtro para selecionar os Boletos de Cobrança e em seguida selecionar os boletos que deverão ser remetidos.

**Dados da Remessa Cobrança Eletrônica**

O cadastro da remessa poderá ser feito através do menu Movimentação Bancária / Integração Bancária/ Remessa Bancária ou durante o processo de remessa. Se o arquivo de remessa for gerado no padrão CNAB240, ativando esta opção, serão abertas novas pastas para Dados Adicionais e Mensagens.  
É necessário também informar um diretório onde será salvo o arquivo de remessa.   
Após a remessa, os campos STATUS.CNAB dos Lançamentos e o Status da Remessa e/ou Status da Remessa PIX do Boleto serão atualizados para "Remetido".

**Cancelamento de Remessa**

O cancelamento da remessa de Cobrança e Débito automático é processado pela visão de Boletos. Após o cancelamento da remessa, o código de barras do Boleto/Lançamentos será mantido. Se for necessário inserir novos lançamentos ao Boleto, cancele o boleto anterior que tem o código de barras e gere novo Boleto e respectivo código de Barras.

Após o cancelamento da remessa de Cobrança PIX, será apagado o QR Code, o Link e atualizado o Status da Remessa do PIX do boleto.
