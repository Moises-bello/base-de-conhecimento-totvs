---
content_hash: b4510a60e102a360f5c2253beef71001e9fe70585c268b1b3fb726d7e1dcedfb
fetched_at: '2026-06-29T00:12:07.193641+00:00'
page_id: '921643709'
product: rm
source: tdn-rm
title: Evento Insucesso na Entrega da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+Insucesso+na+Entrega+da+NF-e
version: 25
---

O objetivo deste novo evento fiscal é registrar as operações de transporte que ocorreram, mas que, por algum motivo, não resultaram na conclusão do serviço e na entrega da mercadoria ao destinatário. Isso pode ocorrer, por exemplo, em casos de recusa do destinatário ou não localização do destinatário, entre outras situações.

Por meio deste evento, o remetente tem a possibilidade de registrar, de forma formal, na NF-e que acoberta a entrega, os motivos específicos que impediram a conclusão da entrega da mercadoria. O evento de insucesso tem como finalidade proporcionar um registro completo e transparente da situação, possibilitando o correto acompanhamento e o devido tratamento de eventuais pendências relacionadas à entrega da mercadoria.

Conforme disposto no Ajuste SINIEF 58/2022, de 09 de dezembro de 2022, quando a entrega da mercadoria não envolver um Conhecimento de Transporte Eletrônico (CT-e), mas estiver diretamente vinculada à NF-e, devem ser utilizados os seguintes eventos:

* Insucesso na Entrega da NF-e (tpEvento= 110192);
* Cancelamento do Insucesso na Entrega da NF-e (tpEvento= 110193)

Para realizar o envio do Evento acesse:

***RM → Backoffice → Gestão de Estoque, Compras e Faturamento → Vendas → Documentos Eletrônicos→ Nota Fiscal Eletrônica (NF-e/NFC-e) → Processos → Envio de Eventos***

noneVídeo How TofalsePasso1lefttrue1Regras do Processo

1. É possível enviar múltiplos eventos do tipo '**Insucesso na Entrega da NF-e**', um para cada tentativa de entrega malsucedida.
2. Só é permitido envio do evento para Notas com o Status **Autorizada**.
3. Caso já exista um Evento Pendente para a Nota, não será possível realizar o envio do mesmo. Será necessário consultar a situação do evento pendente antes de prosseguir.
2Regras de Preenchimento

|  |  |  |
| --- | --- | --- |
| **Campos** | **Obrigatório** | **Descrições dos Campos** |
| Data da tentativa | Sim | Deve ser preenchido com a data da realização da tentativa de entrega. |
| Hora da tentativa | Sim | deve ser preenchido com a hora da realização da tentativa de entrega. |
| Latitude | Não | Pode ser preenchido com a coordenada GPS em decimal com valores de 90.000000 |
| Longitude | Não | Pode ser preenchido com a coordenada GPS em decimal com valores de -90.000000 |
| Número de tentativa | Sim | Deve ser preenchido com a Quantidade de tentativas de entrega. |
| Motivo | Sim | Deve ser preenchido o Motivo do Insucesso na Entrega, possuindo **quatro** opções:   * Recebedor não encontrado * Recusa do Recebedor * Endereço inexistente * Outros |
| Justificativa do motivo de insucesso | Não | Deve ser preenchido quando o **Motivo**selecionado for "Outros", sendo obrigatório digitar ao menos 25 caracteres no máximo 250 caracteres. |
| Imagem da Tentativa | Sim | Deve ter algum dos seguintes formatos: jpg, jpeg, gif, bmp ou png. |

3Cancelamento do Insucesso de Entrega 

**Cancelamento do Insucesso de Entrega da NF-e**  
  
O cancelamento pode ser realizado através da opção disponível nos processos do anexo de eventos.

Regras para Cancelamento do Evento:

1. Somente para notas com o Evento Insucesso na Entrega com status de **Autorizada**, desde que ainda não tenha sido autorizado um Evento de Cancelamento;
2. Se já existir um Evento com Status Pendente para esta Nota, o Evento não pode ser enviado;
3. Se houver mais de um Evento Insucesso na Entrega com status de **Autorizada**, os respectivos cancelamentos serão realizados em ordem de envio, iniciando pelo mais antigo.

Informação

**Obs.**:

Essa macro é so para informar que, esse texto abaixo foi escondido porque, o TSS não cancela o evento Evento Insucesso na Entrega especifico conforme orientado acima.

Por isso não é possível definir esse status abaixo, assim que tiver a resposta que será feito o ajuste ou não, decidiremos se esse texto terá sentido.

Após solicitar o cancelamento o evento ficará com o status de **Cancelamento Pendente.**  
  
Será criado um evento de cancelamento com o Status **Pendente** que deverá ser consultado.

Regras para Consulta de Eventos:

1. Necessário um Evento de Cancelamento de Insucesso na Entrega da NF-e**Pendente.**
2. Aplicar apenas para o Evento de Cancelamento de Insucesso na Entrega da NF-e.

Resultado:

1. Evento Cancelamento de Insucesso na Entrega da NF-e com status **Autorizada.**
2. Evento  Insucesso na Entrega da NF-e  com status **Cancelado**.

4Leiaute do Evento

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Detalhes do Evento** | | | | | | | | |
| **#** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** |
| P18 | versao | Detalhamento de Produtos e Serviços | A | P17 | N | 1-1 | 2v2 | Informar o mesmo valor da tag “verEvento”, Versão do grupo de detalhe do evento. |
| P19 | descEvento | Descrição do Evento | E | P17 | N | 1-1 | 5-60 | Veja a descrição do evento, junto com o Tipo de Evento documentado anteriormente. |
| P20 | cOrgaoAutor | Código do Órgão Autor do Evento | E | P17 | N | 1-1 | 2 | Informar o Código da UF da Chave de Acesso para este Evento. |
| P21 | verAplic | Versão do aplicativo do Autor do Evento | E | P17 | C | 1-1 | 1-20 | Versão do aplicativo do Autor do Evento. |
| P30 | dhTentativaEntrega | Data e hora da tentativa de entrega | E | P17 | D | 1-1 | - | Formato= AAAA-MM-DDTHH:MM:SS TZD |
| P31 | nTentativa | Número da tentativa de entrega | E | P17 | N | 0-1 | 3 |  |
| P32 | tpMotivo | Motivo do insucesso | E | P17 | N | 1-1 | 1 | 1 Recebedor não encontrado 2 Recusa do recebedor 3 Endereço inexistente 4 Outros (exige informar justificativa) |
| P33 | xJustMotivo | Justificativa do motivo do insucesso | E | P17 | C | 0-1 | 25-250 | Informar apenas para tpMotivo=4 |
| P34 | latGPS | Latitude do ponto de entrega | E | P17 | N | 0-1 | - |  |
| P35 | longGPS | Longitude do ponto de entrega | E | P17 | N | 0-1 | - |  |
| P36 | hashTentativaEntrega | Hash da tentativa de entrega | E | P17 | C | 1-1 | 28 | Hash SHA-1, no formato Base64, resultante da concatenação de: Chave de Acesso da NF-e + Base64 da imagem capturada na tentativa da entrega (ex: imagem capturada da assinatura eletrônica, digital do recebedor, foto,etc). **Nota 1**: A critério do autor do evento, este campo pode ser utilizado como índice para acesso as informações do Insucesso na Entrega da NF-e. **Nota 2**: A SEFAZ não tem nenhum controle sobre a informação deste campo. |
| P37 | dhHashTentativaEntrega | Data e hora da geração da tentativa de entrega | E | P17 | D | 0-1 | - | Hash da tentativa de entrega. Formato AAAA-MMDDThh:mm:ssTZD. |
