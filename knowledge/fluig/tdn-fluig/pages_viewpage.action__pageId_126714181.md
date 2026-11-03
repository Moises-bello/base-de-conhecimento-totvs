---
content_hash: c3006d1b794b0242599d63114724bd12ff0928a1381d8ab9577eb34b8d28abbf
fetched_at: '2026-06-28T21:35:17.711976+00:00'
page_id: '126714181'
product: fluig
source: tdn-fluig
title: Configuração de Processos com Componentes Avançados (BPMN 2.0)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126714181
version: 14
---

# Índice

none.\*ndicetrue

# Introdução

Uma das novos recursos do Fluig é a possibilidade de utilizar todo um conjunto de novos componentes vindos da notação BPMN 2.0 permitindo não apenas a automação de um processo como também permite a documentação do mesmo para a organização . Esses novos componentes permitem a extensão de funcionalidades já criadas com os antigos componentes e podem ser acessados utilizando o botão BPMN Extendido localizada na barra de ferramentas da sua IDE. Este botão permite alternar entre os modos **Principal** e **Extendido**. Ao ser pressionado este botão terá efeito imediato sobre a palheta de componentes de modelagem de processo .

Ao acessar o modo **BPMN Extendido**você terá um acréscimo de mais 33 novos elementos que poderão ser utilizados em qualquer processo Fluig que você tenha em sua organização hoje estendendo as funcionalidades do mesmo .

# Script condicional

Um dos novos conceitos existentes no BPMN 2.0 foi a adoção de scripts condicionais. Scripts condicionais são desenvolvidos usando a linguagem javascript e permitem ao Fluig consultar serviços externos permitindo a criação de processos mais elaborados. Scripts condicionais geralmente estão atrelados a agendadores que determinam o período ou a frequência no qual esses scripts serão executados. Quando o script conseguir retornar um valor lógico igual a true significa que o script foi executado com sucesso movimentando as solicitações workflow de acordo com elemento de modelagem utilizado. Maiores detalhes sob como funciona e exemplos de uso podem ser encontrados neste artigo dedicado a .

# Sinal

Sinais é uma nova forma de comunicação entre processos criado para o fluig. Utilizando sinais é possível que um processo mova ou inicie uma ou mais solicitações workflow de acordo com o sinal configurado. A melhor forma de descrever o funcionamento do mesmo com um exemplo . No processo abaixo temos um processo de venda de automóvel em que o cliente acabou de confirmar a compra do mesmo. A atividade seguinte a atividade de compra é um evento intermediário de envio de sinal que possui um sinal chamado "VendaEfetivada" configurada.

O evento intermediário emite o sinal e avança imediatamente para a próxima atividade permitindo ao cliente retirar imediatamente o seu automóvel.  A empresa que vendeu o carro possui um setor de seguros que tem um processo integrado por sinal . Aguarda a confirmação da compra do cliente para imediatamente começar a montar a apólice do seguro e procurar o cliente oferecendo o seguro para o automóvel.

O processo do setor de seguros possui um evento inicial de recepção de sinal . Toda vez que a loja confirma a venda de automóvel automáticamente é aberta uma nova solicitação de workflow no processo de seguros que pouco tempo depois já procura o cliente para oferecer uma proposta de seguro .

Neste meio tempo a fábrica de automóveis que já tem automóveis prontos no estoque também está monitorando o mesmo sinal enviado pela loja e movimenta o seu processo de repor os automóveis da loja.

Apenas configurando os sinais que os eventos estão operando é possível criar um novo tipo de integração entre diferentes processos de diferentes setores sem necessidade nenhuma de programação ou customização adicional.

Observação

Para o completo entendimento deste guia é necessário que o utilizador tenha conhecimento sólido sobre o modo BPMN Principal. Caso contrário solicite treinamento na Academia TOTVS.
