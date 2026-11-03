---
content_hash: aea6acf95b88b5b059a67ff496b31df8d945c4a7c375220ce4f857b6d01ee996
fetched_at: '2026-06-29T00:09:12.841540+00:00'
page_id: '417700621'
product: rm
source: tdn-rm
title: Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Unidade+de+Atendimento
version: 9
---

sumarioUnidade de Atendimento

**Unidades de Atendimento**

---

Nesta interface devem ser cadastradas todas as unidades de atendimento e/ou faturamento. Deve haver ao menos uma unidade de faturamento cadastrada, e com a obrigatoriedade de relacioná-la a um Centro de Custo. A Unidade de Faturamento funcionará como Unidade de Atendimento e de Faturamento, para isso, deverá ser indicado o prestador principal. A Unidade de Atendimento deve, obrigatoriamente, ser associada a uma Unidade de Faturamento. Toda Unidade deve obrigatoriamente ser associada a um Centro de Custo. Para a Unidade que fará atendimentos em regime interno, o Centro de Custo associado deve ter a propriedade "Internação" marcada.

**Outros Dados:**  
Nesta função, são definidos os Dados para emissão de Exame, e o tipo de Prescrição Médica para a Unidade de Atendimento. Os tipos principais são:  
Completa: Exibe a Prescrição Médica de forma completa. Usada principalmente para Unidades de Atendimento do tipo Internação  
Receituário: Exibe a Prescrição de forma mais compacta, um receituário médico. Usada principalmente para Unidades de Atendimento do tipo Atendimento  
Ambas: Exibe ambas as formas, dependendo do tipo de atendimento da Unidade de Atendimento

**Processos farmacêutico:**  
Permite configurar como deve ser o processo de envio e recebimento de pacote. Nessa aba pode configurar se utilizar o fluxo de recebimento pela enfermagem e/ou utiliza o fluxo de entrega de pacote pela farmácia.

**Observação:**  
Para exibição de Prescrição do tipo Prescrição / Receita Medica:   
1 - Parâmetro "Receituário" ou "Ambos", marcado, o paciente com atendimento "Externo", e a Unidade de Atendimento não pode ser "Central de Exames", "Laboratório" ou "Diagnóstico por Imagem";  
2 - O perfil do usuário deve permitir acesso à "Prescrição".  
Para exibição de Prescrição do tipo Prescrição / Exames:  
1 - Parâmetro "Receituário" ou "Ambos", marcado, o paciente com atendimento "Externo", e a Unidade de Atendimento é "Central de Exames", "Laboratório" ou "Diagnóstico por Imagem";  
Para exibição de Prescrição do tipo Prescrição Médica:  
1 - Parâmetro "Completa" ou "Ambos", marcado, o paciente com atendimento "Externo", e a Unidade de Atendimento não pode ser "Central de Exames", "Laboratório" ou "Diagnóstico por Imagem";  
2 - O perfil do usuário deve permitir acesso à "Prescrição Médica".  
3 - O paciente com atendimento "Interno" e o perfil do usuário permitir acesso à pasta "Prescrição Médica".  
Relatórios  
Nesta função, são definidos os relatórios que serão exibidos automaticamente para a Unidade de Atendimento em questão, no momento da conclusão de um registro na Unidade de Atendimento em questão.

PEP RM

**PEP RM**

Selecionando a opção "*Pré-aprazamento como default para lançamento de cuidados*", sempre que for inserido um item na prescrição de enfermagem, o sistema deverá exibir o checkbox de "pré-aprazamento" selecionado com os campos habilitados.

**Observação:**  
Os relatórios devem ser criados no Gerador de Relatórios e conter os parâmetros: CODCOLIGADA, CODPACIENTE e CODATENDIMENTO obrigatoriamente.  
   
O campo "Validar retorno de Consulta" no cadastro de Unidades de Atendimento. De acordo com o parâmetro, o sistema deve validar ou não o retorno de consulta. Até hoje o sistema vazia a validação sem restrições.  
A implementação foi feita no Registro de Atendimento Externo e Elaboração de Conta (Honorários e Exames).

**Observação:**   
Cadastro de unidade de atendimento não pode repetir o mesmo centro de custo na mesma coligada. Mas este mesmo centro de custo poderá estar em outra coligada diferente.  
[clicando aqui](http://totvsconnect.blogspot.com/2011/03/dica-unidade-de-atendimento-totvs).
