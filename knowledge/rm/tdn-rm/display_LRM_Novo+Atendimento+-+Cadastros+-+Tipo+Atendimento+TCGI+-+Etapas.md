---
content_hash: aba2592046dcdbe9ac07839050e72ddc4c54e79cd4be311355696cc3340eb566
fetched_at: '2026-06-29T00:11:28.188016+00:00'
page_id: '730532435'
product: rm
source: tdn-rm
title: Novo Atendimento - Cadastros - Tipo Atendimento TCGI - Etapas
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI+-+Etapas
version: 3
---

O cadastro das ***Etapas do Tipo de Atendimento*** do TCGI está acessível através do menu de Anexos do cadastro e da visão dos **[Tipos de Atendimento](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI)** deste módulo.

Este cadastro foi criado para se ter um melhor controle dos Avanços das Etapas relativos aos Atendimentos do TCGI e ao incluir ou editar esta Entidade o sistema apresenta uma tela com os seguintes campos:

**Etapa do Tipo de Atendimento:** Este campo não é editável e apresenta o Código de Identificação da Etapa do Tipo de Atendimento  selecionado na visão. No momento de inclusão deste novo registro, o mesmo apresenta o valor padrão 0, que será substituído posteriormente, pelo Código de Identificação gerado automaticamente pelo sistema ao salvar esta Entidade;

**Tipo de Atendimento:** Este campo não é editável, sendo preenchido automaticamente pelo sistema, com base no Código de Identificação e na Descrição do Tipo de Atendimento selecionado quando da abertura deste anexo;

**Etapa do Tipo de Atendimento:** Informe neste campo o Identificador ou a Descrição da [Etapa](https://tdn.totvs.com/display/LRM/Etapas) do Tipo de Atendimento do *TOTVS Aprovações e Atendimento* (TAA).  Lembrando que este Tipo de Atendimento do TAA ao qual o Atendimento do TCGI está associado, já foi informado no campo *Tipo de Atendimento*, da tela de cadastro do [Tipo de Atendimento do TCGI](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI).

Uma *Etapa* já parametrizada para o *Tipo de Atendimento do TCGI*, não aparecera mais disponível na listagem para uma nova associação a um Tipo de Atendimento. O usuário poderá editá-la , uma vez que já foi incluída.

É obrigatório informar pelo menos um dos dois campos abaixo em cada uma das *Etapas* criadas:

**Parâmetro para Geração de Movimento do Avanço de Etapa:** Informe o Código ou a Descrição do [Parâmetro para a Geração de Movimento para esta Etapa](https://tdn.totvs.com/pages/viewpage.action?pageId=435105038). O Tipo de *Geração do Movimento* definido neste parâmetro deve ser *Movimento de Atendimento*.

**Lista de Verificação para Avanço da Etapa do Atendimento:** Informe o Código ou a Descrição da Lista de Verificação para Avanço de Etapa, que é um Checklist cadastrado previamente;
