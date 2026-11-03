---
content_hash: 93caec30a33e4ee61f122567e0849f974b4b12d592b360a790b3e2eb4707bc2f
fetched_at: '2026-06-29T00:06:03.633391+00:00'
page_id: '200901651'
product: rm
source: tdn-rm
title: DT_CENTRAL_NOTIFICACOES
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CENTRAL_NOTIFICACOES
version: 1
---

# Central de Notificações - cadastro de mensagens para envio por e-mail

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Educacional, Gestão Bibliotecária e Avaliação e Pesquisa |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetros Educacional | Educacional | Parâmetros | | Parâmetros Gestão Bibliotecária | Gestão Bibliotecária | Parâmetros | | Parâmetros Avaliação e Pesquisa | Avaliação e Pesquisa | Parâmetros |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parâmetros Secretaria Lista de Espera Reserva Recurso / Instalação | Educacional | Parâmetros | Secretaria | Geral 3/5 | | Parâmetros Estágio Envio E-mail Candidatos Alteração Vagas | Educacional | Parâmetros | Estágio | Estágio 1/6 | | Parâmetros Estágio Envio E-mail Aluno Selecionado Vaga | Educacional | Parâmetros | Estágio | Estágio 3/6 | | Parâmetros Estágio Envio E-mail Aluno Não Selecionado Vaga | Educacional | Parâmetros | Estágio | Estágio 3/6 | | Parâmetros Estágio Envio E-mail Aprovação Reprovação Plano Atividades | Educacional | Parâmetros | Estágio | Estágio 4/6 | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Reservas Confirmadas | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Empréstimo Atraso | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Devolução Prevista | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Texto Livre | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Reserva Vencida | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Sugestão Compra Adquirida | | Parâmetros Envio de E-mails Processos Biblioteca | Gestão Bibliotecária | Parâmetros / Configurações | Parâmetros do Sistema | Envio de E-mails | Pasta Usuários Área Interesse | | Parâmetros E-mail de Inscrição | Avaliação e Pesquisa | Parâmetros | Parâmetros do Sistema | Envio de Emails | E-mails Inscrição | | Parâmetros E-mail de Inscrição | Alteração Avaliação e Pesquisa | Parâmetros | Parâmetros do Sistema | Envio de Emails | E-mails Resultado | |
| **Requisito (ISSUE):** | PCREQ-5429 |
| **País(es):** | Brasil |
| **Tabelas utilizadas:** | SMENSAGENSNOTIFICACAO |
| **Versões/Release:** | 12.1.7 |

## Descrição

O objetivo dessa nova funcionalidade é retirar das telas de parâmetros dos produtos TOTVS Educacional, TOTVS Gestão Bibliotecária e TOTVS Avaliação e Pesquisa, TODOS os campos onde são definidos textos para envio de mensagens por e-mail por alguma rotina do sistema, iniciando assim, um processo de centralização das mensagens de comunicação com os usuários do sistema e do portal.

Todos os parâmetros do TOTVS Educacional, TOTVS Gestão Bibliotecária e TOTVS Avaliação e Pesquisa que atualmente são campos texto onde o usuário pode escrever um e-mail padrão para ser enviado por algum processo, parte do sistema ou portal educacional, foram retirados da tela de parâmetros e incluídos em uma nova estrutura.

Os pontos do sistema de onde são disparadas as chamadas para envio de mensagens por e-mail não sofreram alteração. Apenas o local de onde essas informações é recuperada é que fio alterado.

## Procedimento para Utilização

No TOTVS Educacional foi criado um novo item de menu com uma nova TAG de segurança. Esse item de menu se chama “Mensagens de notificação” e está incluído dentro do menu “Auxiliares” do grupo de “Currículo e Oferta”, subgrupo Acadêmico.

No TOTVS Gestão Bibliotecária foi criado um novo item de menu com uma nova TAG de segurança. Esse item de menu se chama “Mensagens de notificação” e está incluído dentro do grupo de Cadastros, no novo subgrupo criado chamado Auxiliares.

No TOTVS Avaliação e Pesquisa foi criado um novo item de menu com uma nova TAG de segurança. Esse item de menu se chama “Mensagens de notificação” e está incluído dentro do grupo de Cadastros, subgrupo já existente Auxiliares.

Dessa forma, quando o usuário precisar cadastrar um modelo de texto para ser enviado por e-mail, esse cadastro deverá ser feito nessa nova tela. Além do texto, o usuário também define qual o objetivo da mensagem, selecionando em uma lista suspensa a opção que mais se adequar.
