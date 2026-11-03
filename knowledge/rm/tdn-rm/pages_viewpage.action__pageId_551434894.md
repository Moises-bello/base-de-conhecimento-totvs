---
content_hash: 1d3d08ff14d45c81d883c08823816ea04c287dd8f8c4eaf67e1f0873b2c0d902
fetched_at: '2026-06-29T00:10:43.953616+00:00'
page_id: '551434894'
product: rm
source: tdn-rm
title: 'Módulo: Portal do Aluno - SGE'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551434894
version: 7
---

|  |  |
| --- | --- |
| Descrição | Novidades do Template por Módulo: Portal do Aluno |
| Observações | Aplicável para SESI/SENAI. |

---

# **Módulo: Portal do Aluno**

## LGPD Termo de Consentimento

**Situação / Requisitos**

Devido a lei geral de proteção de dados pessoais, surgiu a necessidade de solicitar aos alunos, pais e responsáveis que acessam o portal do aluno e confirmem o aceite do termo de consentimento e privacidade de cookies utilizados no portal.

**Solução**

Possibilitar que a instituição defina o termo de privacidade e utilização de cookies para o  portal do aluno.

**Parametrização**

É necessário desenvolver um relatório para cada política a ser aceita. Depois de desenvolvidos, eles devem ser vinculados nos parâmetros do sistema, conforme o print abaixo.

Sempre que necessário será exibido para os usuários um dialogo com texto parametrizado e os relatórios de política de privacidade e política de utilização de cookies.

O dialogo de aceite é exibido nas seguintes situações: quando o usuário ainda não deu aceite nas políticas, ou, quando uma nova versão dos relatórios de politica de privacidade e politica de utilização de cookies forem disponibilizados.

## Disponibilização da Funcionalidade de Negociação Online

**Objetivo**

Permitir a negociação de lançamento em aberto pelo portal do aluno

**Solução**

Foi implementada, no novo portal do aluno, a funcionalidade que permite realizar a negociação online. A partir dos lançamentos em aberto e de uma opção de acordo, o aluno pode simular a negociação e visualizar novas parcelas, valores e vencimentos. Também é possível pagar o primeiro lançamento através de boleto ou cartão.

Atenção

O Perfil de Usuário vinculado ao Aluno também deve ser parametrizado para permitir a visualização do Template. Isso é realizado associando o Template de Acordo ao perfil, através do Anexo "Templates de Acordo Financeiro".

**Novo Portal do Aluno**

No Portal, a Negociação Online está disponível no menu: "Negociação on-line".

Na primeira etapa, introdução são exibidos o texto com instruções para o aluno.

 Na etapa "Débitos Financeiros“, o usuário deverá selecionar os lançamentos/boletos que deseja negociar.

Na etapa "Formas de Pagamento", é apresentado o total dos lançamentos/boletos selecionados na etapa anterior e, a partir da seleção do template de acordo desejado, será possível realizar a simulação para verificar como ficará o acordo.

Caso o usuário queira, poderá imprimir a simulação realizada através do botão "Imprimir simulação“

Na etapa seguinte, "Confirmação", caso esteja parametrizado, será apresentado o termo de aceite para que o usuário leia e aceite. Após o aceite, o usuário poderá confirmar a negociação.

O documento deverá ser aceito no fim da página.

Após confirmar a negociação, será exibida mensagem indicando que o acordo foi realizado com sucesso, e listando as opções de pagamento disponíveis.

## Tutorial de Seleção de Disciplinas na Rematrícula do Ensino Superior

**Situação / Requisitos**

Como aluno, eu preciso de uma instrução sobre a funcionalidade de seleção de disciplinas, para conseguir visualizar as possibilidades que a funcionalidade dá para realizar a rematrícula.

**Solução**

Foi desenvolvido, na tela de seleção de disciplinas, na matrícula online, um tutorial interativo, que ao entrar na tela pela primeira vez, o aluno seguirá os passos do tutorial para conseguir visualizar as funcionalidades da tela.

Ao finalizar o tutorial, ou pular o tutorial, o mesmo não será mais exibido automaticamente, para tutoria seja exibido novamente basta clicar no botão de help localizado no canto direito superior.
