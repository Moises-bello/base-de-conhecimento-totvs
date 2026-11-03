---
content_hash: 59fd9dc718273291bbea1d22633ba06656c5e106fe585e451f561542f8a61c47
fetched_at: '2026-06-29T00:11:21.569665+00:00'
page_id: '697266588'
product: rm
source: tdn-rm
title: S-2299/S-2399 - Como gerar Retificação de desligamento (na competência do desligamento)?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697266588
version: 1
---

false

**A partir das Versões:**

* **12.1.22**
* **12.1.23**
* **12.1.24**

# Objetivo:

---

       O objetivo deste documento é trazer informações de como é o processo de retificação de desligamento, mostrando desde a parametrização até o seu cancelamento.

---

1true1Retificação pela Fila de EventosRetificação pela Fila de Eventos

Acessar a Fila de Eventos de Tabelas/Não Periódicos, localizar e selecionar o evento de desligamento que deseja retificar, ir em "Processos" I "Gerar retificação Arquivo eSocial".

Nesse momento o sistema gera um gatilho do tipo "Retificação" com o status "0 - Pendente". O usuário deve Gerar o XML e proceder com a integração com o TAF.

### Observações:

* Apenas será possível realizar a geração da retificação para eventos que estejam com o status igual a 4 - Aceito TAF ou 10 - Aceito RET.
* Não permitimos a geração de retificação para eventos com os status 0 - Pendente, 1 - Gerado, 2 - Erro na Geração, 5 - Erro na Integração, 6 - Rejeitado TAF, 9 - Rejeitado RET e 11 - Excluído RET, pois nesses status o evento ainda não existe no TAF ou no Governo. Também porque nesses status ainda é possível realizar uma nova geração do mesmo XML.
* Não permitimos a geração da retificação para o status 3 - Enviado TAF pois ainda não existe uma resposta se ele foi aceito pelo TAF ou rejeitado.

Caso o evento esteja em status que não é possível realizar a geração da retificação, é importante que execute o processo "Atualizar Status Integração TAF" para que fique em situação consistente e passível de ser retificado.
