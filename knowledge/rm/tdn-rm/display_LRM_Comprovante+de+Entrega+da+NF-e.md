---
content_hash: aae5d226cf8031b1aab6a399f07233ada6fce91a1cbc0ea1c82c8a6ad4698cf0
fetched_at: '2026-06-29T00:11:09.525191+00:00'
page_id: '640189588'
product: rm
source: tdn-rm
title: Comprovante de Entrega da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Comprovante+de+Entrega+da+NF-e
version: 16
---

O Comprovante de Entrega Eletrônico (Canhoto Digital) é um projeto que tem o intuito de substituir o canhoto físico, relacionado a entrega por parte da transportadora ou da empresa (emissora de NF-e) com frota própria.

Para a NF-e, quando a entrega não estiver relacionada com um Conhecimento de Transporte Eletrônico (CT-e), criam-se os eventos abaixo a serem gerados pela empresa emitente da NF-e:

* Comprovante de Entrega da NF-e (tpEvento=110130);
* Cancelamento do Comprovante de Entrega da NF-e (tpEvento=110131).

Para realizar o envio do Evento acesse:

***RM → Backoffice → Gestão de Estoque, Compras e Faturamento → Vendas → Documentos Eletrônicos→ Nota Fiscal Eletrônica (NF-e/NFC-e) → Processos → Envio de Eventos***

noneVídeo How To

648432

falsePasso1left1Regras do Processo

1. Só é possível **enviar 1 evento** do tipo comprovante de entrega da NF-e por vez.
2. Só é permitido envio do evento para documento **modelo 55** NF-e.
2Regras de Preenchimento

1. O campo **Documento** deve ser preenchido com o número do documento de identificação da pessoa que assinou o Comprovante de Entrega da NF-e, aceitando letras e números.
2. O campo **Latitude** pode ser preenchido com a coordenada GPS em decimal com valores de -90 a 90.
3. O campo **Longitude** pode ser preenchido com a coordenada GPS em decimal com valores de -180 a 180.
4. O campo **UF do Autor** será preenchido com o default da UF da filial da NF-e.
5. O campo **Nome** deve ser preenchido com o nome da pessoa que assinou o Comprovante de Entrega da NF-e.
6. Todos os campos em **negrito** presente na tela devem ser preenchidos **obrigatoriamente** para o processo prosseguir.
7. A **imagem do Comprovante** de Entrega deve ter algum dos seguintes formatos: jpg, jpeg, gif, bmp ou png.
3XML

1. A tag **dhEntrega** será preenchido com a concatenação dos campos **Data da Entrega + Hora da Entrega + Time Zone** conforme parametrização Ambiente Evento do campo Identificação do Horário.
2. A tag **descEvento** será preenchida com texto padrão: "Comprovante de Entrega da NF-e".
4Cancelamento Comprovante de Entrega 

**Cancelamento do Comprovante de Entrega NF-e**  
  
O cancelamento pode ser realizado através da opção disponível nos processos do anexo de eventos:

Após solicitar o cancelamento o evento ficará com o status de **Cancelamento Pendente.**  
  
Será criado um evento de cancelamento com o Status **Pendente** que deverá ser consultado.

Regras para Consulta de Eventos:

1. Necessário um Evento de Cancelamento de Comprovante de Entrega**Pendente.**
2. Aplicar apenas para o Evento de Cancelamento de Comprovante de Entrega.
3. Aplicar no Evento de Comprovante de Entrega "Pendente Cancelamento" não é aceito.

Resultado:

1. Evento Cancelamento de Comprovante de Entrega com status **Aceito.**
2. Evento Comprovante de Entrega com status **Cancelado**.
