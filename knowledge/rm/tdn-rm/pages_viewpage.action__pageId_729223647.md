---
content_hash: a67b4f73d72948fea0a52ad46f66c5851cc1a121a46ea49f745fbdaed96db606
fetched_at: '2026-06-29T00:11:27.710709+00:00'
page_id: '729223647'
product: rm
source: tdn-rm
title: Lançamento da Taxa de Inscrição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=729223647
version: 21
---

## 01. **VISÃO GERAL**

Será possível configurar o processo seletivos para gerar lançamentos no TOTVS Gestão financeira e consequentemente também os boletos.

Para que seja gerado o lançamento será necessário realizar no cadastro do processo seletivo o preenchimento dos campos relacionados a informações financeiras, em:

**TOTVS Processo Seletivo| Cadastros| Processo seletivo| Aba Informações Financeiras**

Com o objetivo de auxiliar na validação da parametrização foi disponibilizada a opção "**Testar geração de lançamento**" ao clicar será realizada uma validação prévia da geração de lançamento.

Para saber mais informações sobre:

* Conta caixa / convênio [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845)
* Pagamento com PIX [clique aqui](https://tdn.totvs.com/display/LRM/Pagamento+com+Pix)
* Pagamento com cartão de crédito [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=489766168)
* Boleto registrado [clique aqui](https://tdn.totvs.com/display/LRM/Boleto+Registrado)
Lançamento financeiro em nome do candidato

Acesse Parâmetros | Parâmetros do sistema | Guia: Integração | Subguia: Estoque, compras e faturamento.

Marque a opção "**Gera movimento para a inscrição**" para que o parâmetro de criação de cliente/fornecedor fique habilitado.

Dessa forma, escolha se será o Candidato ou o Responsável financeiro da inscrição:

 Ao habilitar esta opção de configuração a parametrização realizada na guia Informações financeiras do cadastro do processo seletivo, onde é inserido um cliente/fornecedor padrão, é sobreposta.

## **Desconto do lançamento financeiro**

É possível parametrizar na forma de inscrição um desconto a ser aplicado no lançamento financeiro de inscrição, ao processar um desconto o mesmo será guardado no campo "Desconto" do lançamento.

No entanto a partir da **versão 12.1.2406** será possível parametrizar o **TOTVS Processo Seletivo**  para que o valor de desconto seja guardado em um "[Valor de integração](https://tdn.totvs.com/pages/viewpage.action?pageId=532041706)" do lançamento financeiro e não mais no campo desconto do lançamento.

[Clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=425458275) para saber mais sobre a parametrização.

## **Baixa automática de lançamento**

É possível parametrizar o processo seletivo para que baixe automaticamente no **TOTVS Gestão Financeira** lançamento com valor liquido igual a zero. A baixa via ser executada imediatamente após a confirmação da inscrição no portal.

A funcionalidade de baixa automática estará disponível somente a partir da versão 12.1.2302

Este recurso poderá ser habilitado no cadastro do processo seletivo.

Caso esta opção seja habilitada, será obrigatório informar o **"Meio de Pagamento"** que será utilizado para baixar o lançamento e um e-mail que receberá as informações caso ocorra algum erro ao executar a baixa do lançamento.

Os erros ocorridos durante a baixa do lançamento financeiro não impedirão a conclusão da inscrição e também não será apresentados ao candidato no portal no momento da inscrição (para o candidato será transparente), neste caso será encaminhado para o e-mail cadastrado as informações da inscrição juntamente com o log do erro, e com isso o operador do sistema poderá ajustar alguma parametrização e seguir com a baixa manual .

Status da inscrição

Quando o candidato realizar a inscrição no processo seletivo que possuir taxa de inscrição o status da inscrição ficará como "**Inscrito (pendente de confirmação do pagamento)**" até que o boleto seja liquidado.

No então caso a forma de inscrição possua algum desconto de **100%** ou o valor liquido do lançamento financeiro seja igual a zero, o status da inscrição será alterado automaticamente para "**Candidato (inscrição confirmada)**" após a conclusão da inscrição pelo candidato no portal.

Importante

Para para habilitar no cadastro do processo seletivo o parâmetro "**Baixar automaticamente lançamentos com valor liquido igual a zero**" será necessário que exista cadastrado no **RM** um usuário "**RMProcessoSeletivo**", caso contrário vai ocorrer erro ao executar a baixa do lançamento.

Observação: caso o lançamento seja “Baixa contábil” será necessário que o usuário RMProcessoSeletivo tenha um período válido para gerar lançamento contábeis.

Protheus

A partir da versão 12.1.2406 quando integrado ao Protheus, caso o parâmetro "Baixa automática" esteja marcado será obrigatório [parametrizar o sistema para utilizar valor de integração](https://tdn.totvs.com/pages/viewpage.action?pageId=425458275) do TOTVS Financeiro para guardar o desconto.

Outro ponto importante é que não poderá ser marcada a opção “Data de baixa igual ao vencimento”, pois o Protheus possui limitações de inclusão de baixa com data posterior a data atual do sistema, então em casos de geração de lançamento em data inferior a data de vencimento irá acontecer um impedimento.
