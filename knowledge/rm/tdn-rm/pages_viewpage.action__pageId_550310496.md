---
content_hash: de7dc7834615457d8e3c50dad2ea22ebd37d9cb6b28b69907608169dd03797e2
fetched_at: '2026-06-29T00:10:43.205522+00:00'
page_id: '550310496'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Permissão por Perfil de Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=550310496
version: 3
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de Utilização**

sumarioVisão Geral

# **01. Visão Geral**

Os perfis de **Administrador** do sistema podem executar o registro de atendimento sem nenhuma restrição de acesso independente dos demais acessos de usuário;

Exemplo de Utilização

# **02. Exemplo de Utilização**

Os perfis são configurados através do S**erviço Globais> Segurança > Acesso> Perfis**

1. Caso o usuário não seja administrador do sistema e possa registrar os seguintes empreendimentos:
   1. Perfil de **Pronto Atendimento** terá permissão para realizar apenas o Atendimento Externo (Campo Tipo Paciente: Externo e Pré-Registro Externo)
   2. Perfil de **Internação** terá permissão para realizar apenas atendimento Interno: Atendimento Interno (Campo Tipo Paciente: Interno e Pré-Registro Interno)
   3. Perfil de **Faturamento**:
      1. Podem registrar o atendimento interno: Caso o parâmetro da estação de trabalho "Registra Atendimento? - de Pacientes INTERNOS" esteja marcado.
      2. Podem registrar o atendimento externo: Caso ou parâmetro da estação de trabalho "Registra Atendimento? - de Pacientes EXTERNOS" esteja marcado.
      3. Caso o usuário seja um perfil de faturamento, mas não tenha nenhum desses dois acessos, ele não poderá registrar atendimento, apenas consultas.
   4. Independente do perfil do usuário, se uma estação de trabalho do usuário estiver configurada como **Unidade de Diagnóstico** (uma unidade de atendimento configurada na estação de trabalho está configurada como Laboratório ou Diagnóstico por imagem) o usuário poderá realizar o atendimento Interno ou Externo.
