---
content_hash: 3322f8bca963cf8279225ccdacec3de66f27171bf721d63658487af396775111
fetched_at: '2026-06-29T00:09:14.315963+00:00'
page_id: '421385196'
product: rm
source: tdn-rm
title: Mobilidade (F6)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385196
version: 36
---

---

**Planilha para Apontamentos**

---

Este parâmetro determina qual planilha será utilizada nos apontamentos realizados no aplicativo **Minha Obra**.

As opções disponíveis são: **Planilha de Atividades** ou **Planilha Executiva**.

A configuração desse parâmetro segue as seguintes regras:

1. **Projetos com apontamentos ou folha de tarefa existente:**

   * Quando o projeto já possui apontamentos ou folha de tarefa, a **Planilha de Atividades** será automaticamente habilitada como padrão, sem possibilidade de alteração.
2. **Novos projetos sem apontamentos:**

   * Para novos projetos sem apontamentos, será possível escolher entre as duas opções, desde que o parâmetro **Planilha Executiva** esteja habilitado.
3. **Quando a Planilha Executiva não for utilizada:**

   * Se o parâmetro **Planilha Executiva** estiver desabilitado, a opção **Planilha de Atividades** será selecionada automaticamente, e a **Planilha Executiva** ficará indisponível.

---

**Enviar e-mail de log de erros:**

---

O parâmetro "Enviar e-mail de log de erros" define se haverá o envio de e-mail com um texto padrão para o usuário ou um grupo de usuários do sistema (este grupo deve ser criado pelo próprio cliente, conforme modelo de envio de e-mail para um grupo assim como é feito no Outlook), e que receberá informações do log de erros das importações/exportações realizadas pelos coletores móveis, através dos webservices disponibilizados no projeto Mobilidade.

Para configurar o envio de e-mails na Linha RM, veja em:

[Envio de email - LINHA RM](https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM)

---

**Apontamentos retroativos**

---

O parâmetro Número de dias para apontamentos retroativos ' determina o número máximo de dias que um usuário pode retroceder dos apontamentos de: **Avanço Físico**, **Mão de Obra**, **Equipamentos** e **Ciclo de transporte**.

* Ao deixar o parâmetro em branco o cliente poderá fazer apontamentos com qualquer data retroativa.
* Ao configurar este parâmetro como 0 (zero), o sistema não permitirá que nenhum apontamento tenha data anterior à data atual, para nenhuma das funcionalidades selecionadas. Ao definir um valor numérico maior que zero, o sistema permitirá que apontamentos tenham datas anteriores à data atual, desde que não ultrapassem o número de dias configurado.

**Exemplo com o parâmetro marcado no apontamento de Mão de Obra:**

| Data de inclusão do apontamento | Número de dias para apontamento retroativo | Data de Entrada no Apontamento | APP Minha Obra |
| --- | --- | --- | --- |
| 26/07/2024 | 2 | 26/07/2024 | Permite apontamento |
| 26/07/2024 | 2 | 25/07/2024 | Permite apontamento |
| 26/07/2024 | 2 | 24/07/2024 | Permite apontamento |
| 26/07/2024 | 2 | 23/07/2024 | Não Permite apontamento |

**Funcionalidades e seus parâmetros**

---

[Apropriação](http://tdn.totvs.com/pages/viewpage.action?pageId=421385211)

[Mão de obra](https://tdn.totvs.com/pages/viewpage.action?pageId=662413804)

[Equipamento](https://tdn.totvs.com/pages/viewpage.action?pageId=786539138)

[Ciclo de Transporte](https://tdn.totvs.com/pages/viewpage.action?pageId=662419328)

[Turnos](https://tdn.totvs.com/pages/viewpage.action?pageId=780026691)
