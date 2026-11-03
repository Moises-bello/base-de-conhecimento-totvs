---
content_hash: 3f033adcee68c2bcaac8c5df7e9d392bd1871824040be7e7f9c91d8c483c2482
fetched_at: '2026-06-29T00:10:01.536062+00:00'
page_id: '452718767'
product: rm
source: tdn-rm
title: Registros Inativos a Desconsiderar
type: documentation
url: https://tdn.totvs.com/display/LRM/Registros+Inativos+a+Desconsiderar
version: 4
---

Nesta etapa do parametrizador será possível configurar o eSocial para desconsiderar os registros inativos dos cadastros de Horários, Funções, Eventos, Seções e Tomadores de Serviço. Ao selecionar um dos parâmetros na tela, os registros inativos serão desconsiderados no processo de Carga Inicial do eSocial ,Validação da Base de dados e Lotação Tributária.  
   
**Observação:**

 Os registros inativos que foram desconsiderados não podem estar associados a nenhum evento do eSocial, caso contrário, o XML será gerado com erro. Exceto quando:

* O parâmetro "Não gerar erro de seção inativa para funcionários demitidos na geração do XML" estiver marcado, pois pode existir a necessidade de pagamento complementar para funcionários demitidos anteriormente e a seção já estar desativada. Neste caso não será exibida a mensagem para funcionários demitidos que a seção está inativa.   
  Exemplo: Função X está como Inativa no cadastro e no parametrizador foi selecionado o campo 'Desconsidera Funções Inativas'. Na geração do XML para um funcionário que esteja alocado nesta função inativa, os eventos 2200 ou 2300 serão gerados com erro.

* For calculado diferença salarial ou rescisão complementar por dissídio, e um evento pago na época está atualmente inativo.  
  Exemplo: Evento Y foi pago a três meses atrás ao funcionário, porém hoje ele está inativo. A diferença salarial calculará a diferença referente a esse evento, e levará nos XML's correspondentes a informação na tag infoPerAnt. Nesse caso, mesmo que o evento esteja inativo, não será apresentada mensagem de erro.

**Atenção:** Para solucionar os erros apresentados no XML, o parâmetro "Inativo" deverá ser desmarcado no cadastro de função e deverá ser feito a inclusão manual do evento S-1030 na Fila de Eventos.

|  |
| --- |
| Informações Complementares |

eSocial

[Parametrizador](http://tdn.totvs.com.br/display/LRM/Parametrizador)
