---
content_hash: a49b6cc543baf64fca93bce31d8d5569d1ab84839c17a4e75ff945c3ee8cdc7a
fetched_at: '2026-06-29T00:05:49.370930+00:00'
page_id: '1040976302'
product: rm
source: tdn-rm
title: 4 - Parametrização Jobs Fracionáveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040976302
version: 6
---

Para que os **processos automáticos do Boleto Híbrido** sejam executados corretamente, é necessário configurar a **Segurança de Jobs Fracionáveis** no TOTVS Gestão Financeira.

Essa configuração permite que o sistema execute o processamento de transações **de forma paralela e otimizada**, dividindo a execução em frações.

No menu do sistema, acesse:

**TOTVS Gestão Financeira → Ambiente → Processos → Segurança de Jobs Fracionáveis**

Ao abrir a tela de filtros, clique em **Fechar** para acessar a listagem de registros existentes.

Na tela de listagem, clique em **Inserir (+)** para criar uma nova configuração.

Preencha os campos conforme o exemplo abaixo:

**Perfil de Usuário**  
Informe o perfil que será utilizado para o **agendamento e execução dos Jobs**.

No exemplo desta documentação, utilizaremos o perfil:

**DBA**

**Classe do Processo**

FinBoletoHibridoAtualizacaoFracionadoProcess

**Número mínimo de frações**

2

**Número máximo de frações**

10 ou mais

Esses valores definem quantas **partes simultâneas** o sistema poderá utilizar para processar as transações.

Após preencher todas as informações:

1. Clique em **Salvar**
2. Em seguida clique em **OK**

A configuração do Job Fracionável estará concluída.

Após a configuração, o sistema estará preparado para:

* Executar o **processamento automático das transações do Boleto Híbrido**
* Dividir o processamento em **múltiplas frações**, melhorando a performance
* Permitir a **execução via agendamento de Jobs**
