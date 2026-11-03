---
content_hash: f1a191c141057d54edb0236f931efb39e990b0fb70ea38362a9c35669da543ed
fetched_at: '2026-06-29T00:09:25.288397+00:00'
page_id: '423938103'
product: rm
source: tdn-rm
title: Enviar CT-e OS2
type: documentation
url: https://tdn.totvs.com/display/LRM/Enviar+CT-e+OS2
version: 5
---

Neste processo serão enviados os CT-es OS, de acordo com os dados informados. Após o envio o status do CT-e OS fica como Autorizado.   
No envio o sistema realiza algumas consistências, havendo problemas o status fica como Rejeitado e após a alteração do impedimento, o CT-e OS pode ser selecionado e reenviado. Na tela de envio temos os campos:  
**Filial:** Informe a filial que deseja enviar o CT-e OS.  
**Tipo de Movimento:** Tipo de movimento do CT-e OS.  
**Data Emissão Inicial:** Data de emissão do movimento. (Pode enviar movimentos dentro de um intervalo de datas)  
**Data Emissão Final:** Data de emissão do movimento. (Pode enviar movimentos dentro de um intervalo de datas)  
**Número Inicial:** Número do primeiro movimento do CT-e OS a ser enviado. (Pode enviar movimentos dentro de um intervalo de números)  
**Número Final:** Número do último movimento do CT-e OS a ser enviado. (Pode enviar movimentos dentro de um intervalo de números)  
**Parâmetros do Processo:** Ao clicar nesse botão, serão exibidas informações dos parâmetros configurados para o processo. Após o envio é gerado o registro do CT-e OS na tela de Conhecimento de Transporte Eletrônico para Outros Serviços com os seguintes dados:

* **Aba Identificação**

**Id. Movimento:** Número único sequencial do movimento do CT-e OS  
**Status do CT-e:** (opções: Autorizado, Cancelado, Contingência, Evento Pendente, Inconsistente, Inutilização Pendente, Pendente e Rejeitado)  
**Número do Movimento:**  Número do movimento do CT-e OS  
**Código da Filial:** Filial do CT-e OS  
**Código do Tipo de Movimento:** Código do tipo de movimento do CT-e OS  
**Código do Cliente/Fornecedor:** Cliente/Fornecedor do movimento do CT-e OS  
**Data da Emissão:** Data da emissão do CT-e OS  
**Série:** Série do movimento de CT-e OS  
**Data de Autorização:** Data da autorização do CT-e OS  
**Formato de Impressão do DACTE:** Tipo de impressão do DACTE do CT-e OS (só preenchido quando impresso)  
**Chave de Acesso:** Chave de acesso do CT-e OS  
**Número do Protocolo:** Protocolo junto a SEFAZ do CT-e (só preenchido quando autorizado)  
**E-mail foi enviado:** Flag para indicar se e-mail foi ou não enviado  
**Emitido em Contingência:** Flag para indicar se foi emitido ou não em Contingência  
**DACTE foi impressa:** Flag para indicar se DACTE foi ou não impressa  
**Aba XML:**Contém o XML do CT-e OS.  
***Observação***: Quando utilizado o Client Neogrid, para cada CT-e OS enviado é gerado um XML, que primeiro vai para a pasta OUT e após processamento da ferramenta, é enviado para a pasta SENT, e assim será enviado para a Neogrid. Essas pastas ficam no diretório onde o Client Neogrid está instalado.

Informações Adicionais

* # [TOTVS Colaboração 2.00 - Client Neogrid](http://tdn.totvs.com/pages/viewpage.action?pageId=423938263)
* # [Monitor de Arquivos TOTVS Colaboração](http://tdn.totvs.com/display/LRM/Monitor+de+Arquivos+XML)
