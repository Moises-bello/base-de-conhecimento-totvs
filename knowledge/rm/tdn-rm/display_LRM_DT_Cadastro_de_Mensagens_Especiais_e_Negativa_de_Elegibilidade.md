---
content_hash: 645da0ad2b21d01848dd0185150aaf132d4f7804dd3a40a45ee1ee4457d9c013
fetched_at: '2026-06-29T00:06:07.067329+00:00'
page_id: '201734784'
product: rm
source: tdn-rm
title: DT_Cadastro_de_Mensagens_Especiais_e_Negativa_de_Elegibilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Cadastro_de_Mensagens_Especiais_e_Negativa_de_Elegibilidade
version: 5
---

# Cadastro de Mensagens Especiais e Negativa de Elegibilidade

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | Cadastros |
| **Requisito (ISSUE):** | PCREQ-6791 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e ORACLE |
| **Tabelas utilizadas:** | SZMENSNEGELEGIBILIDADE e SZMENSAGENSESPECIAIS |
| **Sistema(s) operacional(is):** | Windows |
| **Versões/Release:** | 12.1.7 |

## Descrição

**Cadastro de mensagens especiais**:

No Atendimento e Agendamento, ao informar uma carteira de paciente, o sistema validará a máscara e a carteirinha digitada e caso a validação seja positiva, será exibida na tela a mensagem cadastrada. Caso o convênio seja escolhido no cadastro e no atendimento o usuário tenha escolhido um convênio diferente, o sistema irá altera-lo automaticamente.

**Cadastro de negativa de elegibilidade**:

No Atendimento, ao validar a elegibilidade e receber o retorno da TISS online, o sistema validará se a mensagem retornada no XML contém alguma das mensagens cadastradas no sistema e, caso a opção de bloquear atendimento esteja marcada, o sistema realizará o bloqueio do atendimento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação da release 12.1.7

1. Aplique o pacote da release 12.1.7 e execute o agendamento de exames pela assistente

## Procedimento para Utilização

**Exemplo:**

**Cadastro de mensagens especiais**

1. Acesse **Cadastros / Registro e Controle / Mensagens especiais**.
2. Cadastre uma nova mensagem sem escolher o convênio, colocando apenas os campos obrigatórios. Exemplo de máscara: 002600#####
3. No caso acima, todas as carteirinhas digitadas que contenham o número 002600 no início e qualquer número nas posições dos # exibirão a mensagem cadastrada ao sair do campo Cód Usuario Convênio no atendimento interno/externo e no agendamento. Observação: A quantidade de # na máscara influi diretamente na validação pois caso a máscara tenha por exemplo, 6 números e 4 hashtags, apenas carteirinhas com 10 dígitos serão validadas.
4. Faça um novo cadastro agora definindo um convênio.
5. Ao realizar um agendamento ou atendimento e digitar uma carteira que seja validada pela máscara, o sistema irá verificar se o convênio escolhido é o mesmo daquele definido no cadastro das mensagens e caso seja diferente, o sistema altera automaticamente.

**Cadastro negativa de elegibilidade**

1. Acesse **Cadastros / Uso geral / TISS /****Mensagens de negativa de elegibilidade**.
2. Cadastre uma nova mensagem e marque a opção **Bloquear Atendimento**.
3. Realize um atendimento externo e escolha um convênio que tenha webservice TISS para elegibilidade cadastrado.
4. Ao verificar a elegibilidade, o sistema irá receber um XML como retorno do TISS. Se a elegibilidade for negada, os motivos de negativa do convênio estarão no XML. O sistema irá percorrer o cadastro das mensagens e caso o código de alguma negativa esteja cadastrado para e com a opção de bloqueio ativa, o sistema bloqueará o atendimento.
