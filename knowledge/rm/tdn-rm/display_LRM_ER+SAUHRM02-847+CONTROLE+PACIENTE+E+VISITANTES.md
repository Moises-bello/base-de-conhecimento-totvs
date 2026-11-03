---
content_hash: 6ba0aabb8bc353eeef11e19a7b50e228621e5d971cba70e95775f65369576c24
fetched_at: '2026-06-29T00:08:30.225129+00:00'
page_id: '272412485'
product: rm
source: tdn-rm
title: ER SAUHRM02-847 CONTROLE PACIENTE E VISITANTES
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-847+CONTROLE+PACIENTE+E+VISITANTES
version: 4
---

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| Produto | GESTÃO HOSPITALAR - RM | Módulo | **ATENDIMENTO** |
| Segmento Executor | Saúde |  |  |
| Projeto | SAUHRM02 | IRM | SAUHRM02-846 |
| Requisito | SAUHRM02-847 | SubTarefa | SAUHRM02-868 |
| Chamado | 198071 |  |  |
| País | ( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador   (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. |  |  |

# Objetivo

Gerenciar a entrada e saída de pacientes e acompanhantes através de controle via sistema.

* Pacientes – Controlar a permanência do mesmo dentro da instituição, gerenciar se o mesmo realizou todos os exames agendados;
* Acompanhante – Controlar a permanência do mesmo dentro da instituição.

# Definição da Regra de Negócio

**RN001** – **CADASTROS** - Utilizar as funcionalidades já existentes no sistema(TELAS em RI-001);

* Cadastro de cartão de visitantes;
  + Servirá para cadastramento de uma numeração de cartões pré existentes;
    - Este deverá ser desvinculado da informação de leito (Parâmetro).
* **Cadastro do visitante;**
  + Poderá ser feito nesta tela caso já se saiba antecipadamente quem são os beneficiários da instituição.
  + O Cadastro também poderá ser feito na tela Principal **OUTROS SETORES**.(Tela 5)
* Tipo de Visitante
  + Servirá para identificar se quem está na instituição é Paciente ou Acompanhante;
* **Criação de Cadastro de motivos de saídas sem realização de exames(tela 6);**

**RN002** – **PARAMETROS GERAIS E POR ESTAÇÃO DE TRABALHO – (Tela em RI-002);**

1. Criar parâmetro para não associar o leito ao número do cartão de Visitantes;
2. Criar parâmetro para controle de associação de **Atendimento ao número do cartão de identificação do paciente**;
3. Criar parâmetro para trazer por default o tipo de cartão a ser utilizado;
4. Criar parâmetro para trazer por default o setor que visitante ira;
5. Criar parâmetro para trazer por default o tipo de visitante;

**RN003** – **REGISTRO DE ATENDIMENTO** (**Telas em RI-003**);

1. No registro de atendimento se o parâmetro "Associar o atendimento ao número do cartão de identificação do paciente" estiver marcado ;
   * O sistema abrirá uma tela para associar o número do cartão ao registro de atendimento. Esta associação servirá para verificar as pendências de execução de exames no momento da saída do paciente (Tela 8);
   * Se houver o acesso do paciente sem que o mesmo seja identificado na portaria, ao ser recepcionado ,o sistema fara a abertura da tela para associar o número do cartão ao atendimento. Se este ainda não estiver cadastrado o sistema abrirá uma tela para efetuar este cadastro e posterior associação ao atendimento tela 8.1.
     + O Sistema deverá incluir o paciente no cadastro de visitantes automaticamente;
     + Os dados para este novo cadastro deverão vir preenchidos automaticamente(dados do registro de atendimento).

**RN004** – **MENU CONTROLE DE VISITANTES.**

* + Ao clicar na tela atendimento/ Controle de visitantes, abrir a tela de Outros setores sem a necessidade de informação de leitos, caso o parâmetro **RN002** estiver marcado;

**RN005 –** **TELA OUTROS SETORES (Telas RI-004).**

* Criar filtro para selecionar ATIVOS – Quem ainda está na instituição e Inativos – Quem Já Saiu da Instituição (Tela 9)
  + Ativos
  + Inativos
* Criar funcionalidade para que no campo "Número do Cartão" após receber este e logo clique no sinal **MENOS "-"** o sistema já inative o paciente ou visitante**.(Tela 9).**
* Criar funcionalidade para que no campo "Número do Cartão" após receber este e logo clique no sinal **MAIS "+"** o sistema Abra a tela para cadastramento de Visitantes**.(Tela 10);**
  + **Nesta tela o cliente poderá escolher qual tipo de cartão ele usará.**
* Criar funcionalidade para;
  + Se na saída do paciente o sistema identificar pelo campo status (nas tela de Painel Eletivo e de Classificação de Risco) que o mesmo é diferente de "Finalizado" abrirá uma tela com a informação referentes aos exames faltantes**.(Tela 11)**
  + Exibir pergunta se paciente realmente quer sair sem realizar exames;
    - Se sim, sistema abrirá um tela para que o atendente possa escolher o motivo da saída.(Pré cadastrada em motivos de saídas sem realização de exames).

**RN006 – LOG ENTRADA E****SAÍDA**

* + Utilizar esta funcionalidade na tela de Outros setores**(Telas - RI-005);**
    - Incluir SETOR;
    - Incluir coluna de "NOME DO EXAME";
    - Tipo de Visitante – Paciente, Acompanhante;
    - Justificativa (Retirada do motivos de saídas sem realização de exames);

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Registro de Atendimento Externos | Inclusão | Atendimento /Pronto atendimento / Ambulatório/ Registro de Atendimentos Externos/ Exames solicitados |

# Escopo Negativo

* Processo exclusivo para atendimentos externos que utilizam os painéis de classificação de risco e Eletivos;
* O Relatório de etiquetas para paciente visitante será de responsabilidade do cliente;

# Protótipo de Tela

|  |  |
| --- | --- |
| **Regras da Interface** |  |
| **RI-001** | Tela 1 Cadastros              Tela 2 - Cadastro do Cartão – O Informação do Leito não será necessária;   Este cadastro é para clientes que utilizarão cartões com numeração fixa.   Se não for usar esta funcionalidade não será preciso o cadastro destes.        Tela 3 – Tipo de Visitante.      Tela 4 – Criação do menu - Motivos de Saídas sem realização de Exames.   Cadastro justificativa para saída do paciente com falta de execução de exames          . Tela 5 - O Paciente / Acompanhante pode ser cadastrado diretamente nesta tela. Porém o código do cartão será gerado aleatoriamente.          Tela 6– Cadastro dos Motivos para registro de pacientes que não realizaram todos exames e saíram da Instituição. |
| **RI-002** | Tela 7 – Criação dos parâmetros. |
| **RI-003** | Tela 8 – Após cliente salvar o Atendimento será aberta uma tela para vincular o número do cartão ao Atendimento do paciente.        Tela 8.1   Se o paciente não foi cadastrado na portaria, ao chegar na recepção o atendente poderá efetuar o cadastro de visitantes para o mesmo. Estes dados deverão vir preenchidos automaticamente. Após o sistema fará o vínculo do cartão com o atendimento(automaticamente). |
| **RI-004** | Tela 9 – Informando o código do cartão e clicando no sinal de "-".        Tela 10 – Cadastro de Visitantes ao Clicar na Tecla **"MAIS" +.**        Tela 11 – Tela de Pendencia de exames. **Nesta tela Obrigar a Justificativa**. |
| **RI-005** | Tela 12 – Filtra para escolha da pesquisa. Ativos, são os pacientes que ainda estão na Instituição. Inativos, são os pacientes que já saíram   O Botão Log entrada e saída demonstrará os pacientes que entraram e saíram da instituição e as Justificativas de não realização de exames.          Tela – 13 – Log de Entrada e Saída. Nesta aparecerão os exames do paciente e a Justificativa da não realização caso ela exista.   Acompanhantes também aparecerão neste log. |

# \_Toc355276667Fluxo do Processo

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.
