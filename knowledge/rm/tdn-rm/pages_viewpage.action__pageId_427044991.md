---
content_hash: 9f2fff3ec7220f2162d738d0d8761cbc6a0ea14be27cf7ce167c58e78d269850
fetched_at: '2026-06-29T00:09:38.539132+00:00'
page_id: '427044991'
product: rm
source: tdn-rm
title: Nome social - Mensagens de notificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=427044991
version: 1
---

# NOME SOCIAL - MENSAGENS DE NOTIFICACAO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | *TOTVS Gestão Educacional* |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Mensagens de notificação | Mensagens de notificação |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Confirmação de reservas de recursos | Reserva de recursos | | Confirmação de reservas de instalação | Reserva de instalações | | Vagas de estágio | Vagas de estágio | | Plano de atividades do estágio | Vagas de estágio | | Convite de banca de estágio | Vagas de estágio | | Aviso de boleto próximo do vencimento | Boleto Financeiro | | Pendências financeiras | Notificação financeira | | Cadastro de ocorrências | Cadastro de ocorrências | | Frequência de alunos | Frequência de alunos | | Digitação de etapa de nota/falta | Digitação de nota/fatla | | Digitação de notas de avaliação | Digitação de nota de avaliação | | Envio de mensagens eventuais | Mensagens eventuais | | Aprovação de inscrições em vista/evento | Projeto Pesquisa, Extensão | | Aviso de frequência de bolsista | Projeto Pesquisa, Extensão | | Notificação sobre relatórios à coordenadores | Projeto Pesquisa, Extensão | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | N/A |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | N/A |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | N/A |
| **Pacote:** | N/A |

## Descrição

Adaptação das mensagens de notificação para exibição do nome social, caso essa informação esteja cadastrada..

Mensagens que foram alteradas para considerarem a informação do nome social, no lugar do nome:

**Grupo Secretaria:**

Confirmar reservas de recursos;

* + - Tags que receberam o tratamento:: *NOMEUSUARIO*

Confirmar reservas de instalações;

* + - Tags que receberam o tratamento:: *NOMEUSUARIO*

**Grupo: Estágio:**

Informar ao aluno que ele foi selecionado para a vaga de estágio na qual está inscrito;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Informar ao aluno que ele não foi selecionado para a vaga de estágio na qual está inscrito;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Informar ao aluno sobre aprovação do plano de atividades do estágio;

* + - Tags que receberam o tratamento:: *NOMEALUNO, NOMEORIENTADOR*

Informar ao aluno sobre reprovação do plano de atividades do estágio;

* + - Tags que receberam o tratamento:: *NOMEALUNO, NOMEORIENTADOR*

Informar para o participante que ele foi convidado para a banca;

* + - Tags que receberam o tratamento:: *NOMEALUNO, NOMEPARTICIPANTE*

**Grupo: Financeiro:**

Próximo boleto ao vencimento;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

**Grupo: Matrícula e Avaliação:**

Pendências financeiras do aluno;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Cadastro de ocorrência para o aluno;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Frequência do aluno próximas do limite ou excedido;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Pendências de matrícula;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Liberação ou digitação de etapa de nota;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Liberação ou digitação de etapa de falta;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Liberação ou digitação de notas de avaliação;

* + - Tags que receberam o tratamento:: *NOMEALUNO*

**Grupo: Mensagens eventuais:**

Enviar mensagens eventuais para e-mail, Fluig ou eduConnect;

* + - Tags que receberam o tratamento:: *NOMEALUNO, NOMERESPONSAVEL, NOMEPROFESSOR, NOMECOORDENADOR, NOMERESPONSAVELACADEMICO, NOMERESPONSAVELFINANCEIRO*

**Grupo: Pesquisa e extensão:**

Aprovação das inscrições da visita/evento (extensão);

* + - Tags que receberam o tratamento:: *NOMEALUNO*

Enviar notificação para aviso de frequência do bolsista;

* + - Tags que receberam o tratamento:: *NOMEBOLSISTA*

Enviar notificação ao coordenador do projeto sobre envio de relatório parcial de acompanhamento;

* + - Tags que receberam o tratamento:: *NOMEPESSOACOORDENADOR*

Enviar notificação ao coordenador do projeto sobre envio de relatório final de acompanhamento;

* + - Tags que receberam o tratamento:: *NOMEPESSOACOORDENADOR*
