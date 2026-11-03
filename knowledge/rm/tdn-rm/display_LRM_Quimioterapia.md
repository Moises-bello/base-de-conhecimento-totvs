---
content_hash: 11d9f8255b0c558e60b009844d342bba1506353442148f295a4ff94e5ee3ab27
fetched_at: '2026-06-29T00:11:11.811915+00:00'
page_id: '650485184'
product: rm
source: tdn-rm
title: Quimioterapia
type: documentation
url: https://tdn.totvs.com/display/LRM/Quimioterapia
version: 17
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Modal de Medicamentos**
4. **Prescrição complementar**
5. **Cálculo de superfície corporal**

Quimioterapia1. Visão Geral

## **01. VISÃO GERAL**

Recurso que permite ao usuário visualizar, iniciar e fazer prescrições da especialidade para o paciente.

2. Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao clicar no menu de Oncologia e na aba de "Quimioterapia" será exibido para o usuário os campos de "Protocolo", "Fase", "Ciclo" e "Data prevista".

Para visualizar os itens de cada ciclo é necessário selecionar ao menos um protocolo, fase e ciclo conforme mensagem em tela. O campo data prevista é opcional.

Ao selecionar um protocolo, fase e ciclo serão listados os dias e os respectivos itens que compõe o ciclo.

O campo data prevista só deverá ficar habilitado quando o usuário selecionar o Ciclo 1, caso contrário deverá ficar desabilitado.

Caso seja selecionado o ciclo 1, serão calculadas as possíveis datas dos dias que compõem o ciclo, com base no intervalo do ciclo dividido pela quantidade de dias a cada ciclo, sendo o D1 a data prevista.

3. Modal de Medicamentos

## **03. MODAL DE MEDICAMENTOS**

No menu de Oncologia, na aba de "Quimioterapia", após selecionar o protocolo, fase e ciclo, após a importação dos itens que compõem o dia, o usuário poderá visualizar os itens e/ou inserir informações.

Para inserir informações o usuário deverá clicar no medicamento para abrir a modal com as seguintes informações:

* Medicamento;
* Bula (se cadastrada no RM);
* Ciclo;
* Dias de aplicação;
* Ordem;
* Categoria;
* Creatinina (caso a unidade da dose cadastrada seja por AUC);
* Via;
* Frequência;
* Dose cadastrada e unidade;
* Dose calculada;
* Componente de diluição (caso possua);
* Administrar solução: Em bolos, gravidade, Bomba de infusão e Medicamento oral, além do tempo de administração.

Todas as informações acima serão herdadas do cadastro do protocolo no RM, caso possuam, exceto a creatinina que é informada no cálculo da dose pelo usuário. Todos deverão estar bloqueados para edição.

Além destes campos será exibido também os campos habilitados para edição:

* Volume;
* Redução do volume;
* Justificativa (caso aplicada redução);
* Observações;

Caso o medicamento tenha configuração de envio de quantidade na unidade de controle para o backoffice e cálculo de dose com opção diferente de FIXO nas configurações do item de medicamento, será utilizada a unidade de dosagem padrão "MG" (miligrama).

Exemplo de configuração do cálculo de dose e envio de quantidade na unidade de controle para o backoffice:

RM > Cadastros > Estoque > Produtos > Selecione o medicamento > Anexos: "Informações - TOTVS Saúde" > Identificação II > Campo "Integração Backoffice" > Campo "Cálculo de dose - Parâmetros PEPRM". 

 

Exemplo de configuração de medicamento com o cálculo de dose com opção diferente de FIXO:

4. Prescrição complementar

## **04. PRESCRIÇÃO COMPLEMENTAR**

O usuário poderá prescrever medicamentos que não foram previamente cadastrados para o protocolo conforme necessidade. Ao clicar no botão para adicionar uma modal será exibida para preenchimento:

Após preencher, ao clicar no botão "Salvar" para adicionar, uma modal será exibida perguntando ao usuário se deseja adicionar o medicamento aos próximos ciclos:

Ao clicar no botão "Finalizar", o medicamento será adicionado.

5. Cálculo de Superfície Corporal

## **05. CÁLCULO DE SUPERFÍCIE CORPORAL**

A superfície corporal é utilizada como base para o cálculo de dose de diversos medicamentos quimioterápicos. Anteriormente, o sistema realizava esse cálculo exclusivamente pelo método de Mosteller.

A partir da versão12.1.2602, o sistema permitirá escolher entre dois métodos: **Mosteller** ou **Du Bois**. Essa melhoria garante maior aderência aos protocolos clínicos adotados por cada instituição.

**Nova parametrização por unidade de atendimento:**

O novo parâmetro está disponível nas configurações de cada unidade de atendimento, no caminho: Aba "Prontuário Eletrônico" > Sub-aba "Oncologia". O usuário poderá definir qual método será aplicado para o cálculo no PEP: Mosteller (padrão do sistema) ou Du Bois.

**Aplicação automática**

O sistema mantém o método Mosteller como padrão e aplicará automaticamente o método configurado na unidade após a alteração. No prontuário, o profissional não precisará selecionar o método manualmente; o sistema realizará o cálculo considerando:

* + Peso (kg)
  + Altura (cm)
  + Resultado: apresentado em m².

**Impacto na prescrição**

O método definido impacta diretamente o valor da superfície corporal e, consequentemente, a dose dos medicamentos calculada com base nessa superfície.

**Método Mosteller:** SC = √((altura x peso) / 3600)

**Método Du Bois:** SC = 0.007184 \* Altura0.725 \* Peso0.425
