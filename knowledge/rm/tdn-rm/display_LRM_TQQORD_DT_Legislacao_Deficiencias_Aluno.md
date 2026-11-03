---
content_hash: 694ff0acfcbca4c9b710cc51bcdb74f8e55feff6df7108af95d7f89ef8647171
fetched_at: '2026-06-29T00:06:21.168000+00:00'
page_id: '223163020'
product: rm
source: tdn-rm
title: TQQORD_DT_Legislacao_Deficiencias_Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/TQQORD_DT_Legislacao_Deficiencias_Aluno
version: 129
---

# ALUNO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | **TOTVS Gestão Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Aluno* | *Cadastro de Aluno* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | **Censo Escolar** | *Processo de envio de informações do Censo*  *Anexo Dados do Censo Escolar e SISTEC* | |  |  | |
| **Cadastros Iniciais:** | *Pessoa e Aluno* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *Currículo e Oferta | Aluno e Professor | Alunos* |
| **Chamados Relacionados** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e ORACLE* |
| **Tabelas Utilizadas:** | *SALUNO, SALUNOMEC, PPESSOA* |
| **Sistema(s) Operacional(is):** | *N/A* |
| **Versões/Release:** | *11.83.55.221*  *12.1.11* |

## Descrição

Nesta implementação foi realizada uma reformulação dos campos referentes a deficiências do Aluno para possibilitar maior flexibilidade ao usuário no cadastro destas informações no Sistema.

Foram criadas duas novas abas no cadastro do Aluno: "Pessoas com necessidades educacionais especiais" e "Atendimento Especial".

Além disso, os campos com informações de deficiências do cadastro de Aluno e do anexo Dados do Censo Escolar e SISTEC foram unificados.

Observações:

1. Os seguintes campos estão presentes tanto no cadastro do aluno quanto no cadastro de pessoa:
   1. Fala;
   2. Auditiva;
   3. Visual;
   4. Intelectual;
   5. Física;
   6. Reabilitado (BR).
2. Os campos considerados pelo processo de envio de informações para o Censo são:   
   1. Não possui informações sobre deficiências do aluno;
   2. Surdez;
   3. Múltipla;
   4. Alta Habilidade/Superdotação;
   5. Transtorno do espectro autista;
   6. Surdocegueira;
   7. Baixa visão;
   8. Cegueira;
   9. Intelectual;
   10. Transtorno desintegrativo da infância;
   11. Síndrome de Asperger;
   12. Síndrome de Rett;
   13. Física.
3. Inconsistência na base de dados: quando for identificado uma inconsistência entre os dados referentes a deficiências da pessoa e do aluno, será exibido uma mensagem alertando para que o usuário ajuste estes cadastros. Para correção destas inconsistências o usuário tem a opção de atualizar os cadastros manualmente ou executar script criado para este fim (enviado mediante solicitação).

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado e a execução de script específico (enviado mediante solicitação).

1. Aplique o patch do chamado, execute o script na base de dados e acesse uma vez a rotina *Cadastro de Alunos*.
2. Após isto, estarão disponíveis duas novas abas na pasta Identificação: Pessoa com Deficiência (PCD) e Atendimento Especial.
3. Acesse também o anexo Dados do Censo Escolar e SISTEC. Os campos de deficiências enviadas para o Censo são os mesmos exibidos na nova aba criada no cadastro do Aluno.

## Procedimento para Utilização

       1.            No módulo Educacional, acesse Currículo e Oferta | Aluno e Professor | Alunos.

Após a execução de um filtro, o sistema apresenta a janela de alunos cadastrados para o contexto selecionado.

       2.            Posicione o cursor em um aluno e clique em Alterar.

       3.            Na pasta Identificação selecione a aba Pessoa com Deficiência.

       4.            Informe os dados dos novos campos.

       6.            Confira os dados e confirme.

       7.            Selecione um aluno e abra para edição o anexo Dados do Censo Escolar e SISTEC.

                      Os mesmo campos com dados referentes a deficiências do Aluno são exibidos.

       8.            Confira os dados e confirme.

divs
