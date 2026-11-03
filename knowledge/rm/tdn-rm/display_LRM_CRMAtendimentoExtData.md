---
content_hash: 0ca1028589c52121baf9c6668fb6f905be6b2d530fe34e26d837f10a5b7aec4b
fetched_at: '2026-06-29T00:05:47.742877+00:00'
page_id: '1016666216'
product: rm
source: tdn-rm
title: CRMAtendimentoExtData
type: documentation
url: https://tdn.totvs.com/display/LRM/CRMAtendimentoExtData
version: 3
---

---

**1 - Dados Gerais**

---

* **Produto:** TOTVS CRM
* **Linha:** Linha RM
* **Módulo:** CRM - Atendimento
* **Função:** Consumo REST DataServer via API
* **País:** Brasil
* **Tickets relacionados:** 1485428, 839808, 11885244, 13323721, 16638921

**Requisito:** Solicitação de documentação – DataServer CRMAtendimentoExtData

---

**2 - Operações Suportadas**

---

* **GET:** Leitura (lista e registro) – via DoReadView / DoReadRecord
* **POST:** Inclusão – via DoSaveRecord (com CODATENDIMENTO = -1)
* **PUT:** Alteração – via DoSaveRecord

**Segurança:** Filtro **RMSSecurityFilter (804002000)** limita retorno conforme usuário (responsável atual, histórico, criador ou fila).

---

**3 - Instruções Importantes**

---

* **Separador correto da PK composta:** $\_$
* **Separador incorreto:** $$ (gera erro “Registro não encontrado”)
* **PK composta (ordem):**

CODCOLIGADA | CODLOCAL | CODATENDIMENTO

### **Padrão de URL**

* **GET / PUT (leitura/alteração):**

[http://HOST:PORTA/rmsrestdataserver/rest/CRMAtendimentoExtData/{CODCOLIGADA}$\_${CODLOCAL}$\_${CODATENDIMENTO](http://HOSTPORTA)}

* **POST (inclusão):**

[http://HOST:PORTA/rmsrestdataserver/rest/CRMAtendimentoExtData](http://HOSTPORTA)

Definir "CODATENDIMENTO": -1 no body.

* **PUT alteração:**

<http://localhost:8051/rmsrestdataserver/rest/CRMAtendimentoExtData/1$_$1$_$100>

---

**Exemplos:**

---

### Body mínimo para POST

JSON

{

"CODCOLIGADA": 1,

"CODLOCAL": 1,

"CODATENDIMENTO": -1,

"ASSUNTOOC": "Solicitação de suporte técnico",

"CODGRUPOATENDIMENTO": 4,

"CODTIPOATENDIMENTO": 2,

"CODATENDENTERESP": 9,

"CODCOLIGADARESP": 1,

"PRIORIDADE": 100,

"CODSTATUS": "G"

}

Mostrar mais linhas

Para acrescentar conteúdo sem sobrescrever histórico, usar:  
 TEXTOSOLICITACAO\_NOVO, TEXTODISCUSSAO\_NOVO, TEXTOSOLUCAO\_NOVO

**Campos principais de integração:** ASSUNTOOC, CODSTATUS, CODGRUPOATENDIMENTO, CODTIPOATENDIMENTO, CODATENDENTERESP, CODCOLIGADARESP, PRIORIDADE, PCTPRONTO, CODTAREFA, TEXTOSOLICITACAO\_NOVO, TEXTODISCUSSAO\_NOVO, TEXTOSOLUCAO\_NOVO, TEMANEXO, TEMSOLUCAO, TOTAL\_ANEXOS, DESCSITUACAOATENDIMENTO.

---

**4 - Filtros ($filter)**

---

* RESPONSABLEUSERID eq 'USUARIO' → atendimentos pendentes (status G,T,A,D,R) onde usuário é responsável
* ISHISTORICALUSER eq true → inclui atendimentos que passaram pelo usuário

CREATEDUSERID eq 'USUARIO' → atendimentos criados pelo usuário

---

**5 - Status (CODSTATUS)**

---

* **Pendentes:** G, T, A, D, R

**Finais:** C (concluído - edição limitada), F (fechado - não editável)
