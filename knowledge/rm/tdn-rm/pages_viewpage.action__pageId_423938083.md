---
content_hash: cda457d8f9f7d0e1ec769501eef0f6ba96ab873d9ff4a3b0c6b650b99f3265ab
fetched_at: '2026-06-29T00:09:25.258823+00:00'
page_id: '423938083'
product: rm
source: tdn-rm
title: Enviar Evento (CT-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938083
version: 3
---

**Enviar Evento**

Menu Vendas | Faturamento | Conhecimento de Transporte Eletrônico (CT-e) | Processos  
Esse processo envia eventos do CT-e, como Cancelamento e Carta de Correção. O status do CT-e é alterado para Evento Pendente.

**Cancelamento**

Envia evento de cancelamento para o CT-e autorizado selecionado.  
Selecione um Tipo de Evento – Selecionar o evento.  
Justificativa – Informar uma justificativa para o cancelamento.

**Carta de Correção**

Após a concessão da Autorização de Uso do CT-e, o emitente poderá sanar erros em campos específicos do CT-e, por meio de Carta de Correção Eletrônica - CC-e transmitida à Secretaria da Fazenda.

Não poderão ser sanados erros relacionados:

* As variáveis que determinam o valor do imposto tais como: base de cálculo, alíquota, diferença de preço, quantidade, valor da prestação;
* A correção de dados cadastrais que implique mudança do emitente, tomador, remetente ou do destinatário;
* A data de emissão ou de saída.

O processo está disponível em:

1. Vendas | Faturamento | Conhecimento de Transporte Eletrônico(CT-e);
2. Selecionar o registro de CT-e que possui status de "Autorizado";
3. Acessar o menu Processos | Enviar Evento;
4. Escolher a opção "Carta de Correção" e Avançar;

5. Os campos e opções de alteração variam de acordo com a Modalidade Do CT-e.

**Importante!** Todos os campos passíveis de alteração previstos pelo [Manual da Carta de Correção Eletrônica do CT-e](http://www.cte.ms.gov.br/wp-content/uploads/2015/01/Manual-da-Carta-de-Corre%C3%A7%C3%A3o-eletr%C3%B4nica-do-CT-e_-final.pdf) poderão ser encontrados na tela acima.

***Observação***: Quando utilizado o Client Neogrid, para cada evento de CT-e enviado é gerado um XML, que primeiro vai para a pasta OUT e após processamento da ferramenta, é enviado para a pasta SENT, e assim será enviado para a Neogrid. Essas pastas ficam no diretório onde o Client Neogrid está instalado.
