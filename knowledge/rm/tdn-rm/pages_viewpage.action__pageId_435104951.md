---
content_hash: e91508908d8b894161391203943a6489bf9ef619fc0f8e7efb8dff7483d807f1
fetched_at: '2026-06-29T00:09:47.157001+00:00'
page_id: '435104951'
product: rm
source: tdn-rm
title: Contrato de Locação - Aditivos - Exclusão de Imóvel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104951
version: 11
---

O Aditivo  de Exclusão de Imóvel tem o objetivo de desassociar os imóveis selecionados ao contrato de locação que já foi efetivado e teve seus lançamentos financeiros criados. Através do aditivo é possível também gerar cobrança de multa.   
**Pré-condições**

1. Ter habilitado a permissão [02.03.01.30 e 31] para Efetivar / Desfazer aditivo de Exclusão de Imóvel, do perfil do TOTVS Gestão de Imóveis, localizada em *Serviços Globais / Segurança / Perfis.*
2. Ter efetivado o Contrato de Locação.
3. Ter selecionado um imóvel.
4. Ter incluído um Motivo do Aditivo.

**Incluindo um Aditivo de Exclusão de Imóvel**

* Selecione o Contrato de Locação e acesse: Anexo/Aditivo/Exclusão de Imóvel.
* Clique em Incluir Aditivo de Exclusão de Imóvel. Preencha os campos:

* + Código do Aditivo: Campo de preenchimento automático.
  + Data do Aditivo: Data do cadastro do aditivo.
  + Tipo do Aditivo: Campo de preenchimento automático.
  + Situação do Aditivo: Preparação.
  + Motivo do Aditivo: Informar um Motivo do Aditivo.
  + Número do Aditivo no Cliente: Campo onde o cliente informar o número do Aditivo no Contrato físico. Podendo assim realizar o agrupamento de vários aditivos do sistema a um aditivo físico.

* Informar os imóveis que serão excluídos.
* Caso haja cobrança de multa, preencha o campo Código da Multa com a multa que desejar. É possível usar o botão  para calcular o valor da multa e a memória de cálculo que resultou neste valor.

* Salvar
* Verifique que o status do Aditivo foi alterado para Efetivado.
* Selecione o Aditivo e clique em Editar Aditivo de Exclusão de Imóvel.
* Acesse a aba Histórico. Será exibida a informação  do campo Observação preenchido ao efetivar o Aditivo.

Importante!

* Se o contrato possui uma garantia associada com vinculo ao valor do contrato, (opção "Vínculo com o valor do contrato" no cadastro de garantias), o sistema exigirá, na efetivação do aditivo de exclusão de imóveis, um aditivo de garantia em preparação para ser aplicado. Este aditivo será automaticamente efetivado ao se efetivar o aditivo de exclusão de imóvel;
* O aditivo de exclusão de imóvel deverá possuir o mesmo número do aditivo de garantia "Em Preparação" para que seja efetivado corretamente;
* Da mesma forma, ao desfazer o aditivo de exclusão de imóvel, o sistema automaticamente deverá desfazer o aditivo de garantia e voltar sua situação para "Em Preparação".
* O campo Valor total do distrato**,** disponível a partir da versão 12.1.28, representa o somatório dos valores dos imóveis excluídos através do aditivo.
