---
content_hash: 6253e17c5f32d53baa0fbd45b6d515bc6627b47d0cf289d9bb08ea626bc15929
fetched_at: '2026-06-29T00:08:30.212623+00:00'
page_id: '272411886'
product: rm
source: tdn-rm
title: ER_296828__NOME_EXAMES_NO PAINEL DE ATENDIMENTO
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_296828__NOME_EXAMES_NO+PAINEL+DE+ATENDIMENTO
version: 2
---

\_GoBack

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | ATENDIMENTO |
| Segmento Executor | Saúde |  |  |
| Projeto¹ |  | IRM¹ |  |
| Requisito¹ |  | SubTarefa¹ |  |
| Chamado² | 296828,296569,295173 |  |  |
| Release de Entrega Planejada | Não definido | Réplica | Não necessário |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |
| Outros |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

Permitir que no painel de atendimento eletivo o paciente apareça tantas vezes quanto a quantidade de exames a serem realizados, Assim, a enfermagem poderá visualizar o paciente em mais de uma unidade de atendimento e efetuar a chamada do mesmo conforme tipo de exame e local de atendimento;

# \_Toc355276664Definição da Regra de Negócio

**RN001** – Registro de atendimento – Telas(RI-001).

* O Paciente retirará uma única senha no totem de atendimento.
* No painel de atendimentos eletivo, ao efetuar a chamada do paciente o recepcionista poderá identificar todos agendamentos do paciente para aquele dia;
* O Atendente poderá efetuar o registro de atendimento para cada exame agendado;
* Se houver três exames em horários diferentes e estes forem em setores distintos, será necessário efetuar três atendimentos;
* Inserir o nome do procedimento(Exame) na Grid de Agendamentos do dia (RI-001- Tela Agendamentos do dia);

**RN002** – Painel de chamada – Enfermagem; RI-002 (Tela 1)

* Incluir a Coluna com o nome do exame;
* Incluir a coluna Data do Agendamento;
* Incluir coluna com hora do agendamento;
* Suprimir as colunas "Dt. Triagem" e "Espera" .(  )

**RN003 –** Visualização Exames para chamada da Enfermagem;

* Se o paciente teve em seu registro mais de um atendimento estes deverão aparecer no painel separadamente, porém, com a mesma senha; RI-002 (Tela 1)
* Caso haja dois exames similares exemplo, RX mão direita e RX Mão direita e estes forem no mesmo setor e forem no mesmo atendimento então os mesmos aparecerão no painel uma única vez e os nomes dos exames aparecerão concatenado, mesmo padrão da tela de agendamento - RI-002 (Tela 2 e 3);

**RN004 –** Enquanto o paciente não for chamado o status ficará em "Aguardando", **a**pós chamada da enfermagem para atendimento do paciente, o status do mesmo ficara como "Em atendimento" e só mudará para "Finalizado" no termino do atendimento pela enfermagem (Regra atual dos status do painel);   
 **RN005 –** Criar parâmetro para que na Aleta Posto de Enfermagem possa ser omitido a chamado do Prontuário Eletrônico.

* Se o parâmetro estiver marcado não chamará o Prontuário após a chamada do paciente pela Enfermagem- Ver RI-003

|  |  |  |  |
| --- | --- | --- | --- |
| Rotinas Envolvidas |  |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Registro de Atendimento Externos | Inclusão | Atendimento /Pronto atendimento / Ambulatório/ Registro de Atendimentos Externos/ Exames solicitados |
|  |  |  |

# Escopo Negativo

# \_Toc355276665Protótipo de Tela

|  |  |
| --- | --- |
| \_Toc355276666**Regras da Interface** |  |
| **RI-001** | Na chamada da senha de atendimento permitir que seja feito todos atendimentos. Exemplo: Senha 9 tem três exames para serem realizados.                      Tela Agendamentos do Dia – Incluir nome do procedimento(Exame);      Atendimento 1                  Atendimento 2              Atendimento 3 |
| **RI-002** | Painel Eletivo – Chamada da Enfermagem;     Tela 1 – Três atendimentos diferentes. Note os status (Em atendimento, Aguardando)        Tela 2 – Dois agendamentos para o mesmo horário com dois exames similares e mesmo setor.                                    Tela 3 – Um atendimento com dois exames. |
| **RI-003** | Criação de Parâmetro para que na Aleta Posto de Enfermagem não chame o Prontuário Eletrônico.            Na chamada do paciente a caixa de Diálogo será suprimida e a Finalização do Atendimento será somente pelo botão. |

# \_Toc355276667Fluxo do Processo

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
