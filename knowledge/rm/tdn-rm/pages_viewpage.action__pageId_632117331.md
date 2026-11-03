---
content_hash: 11688757d81f9fe15ee913804a094949c571310b5bebddaece4a71606db4819b
fetched_at: '2026-06-29T00:11:05.535973+00:00'
page_id: '632117331'
product: rm
source: tdn-rm
title: Como gerar a tag <codIncCP> com a incidência 95, 96, 97 ou 98 e extensão da
  decisão/sentença em um evento de desconto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=632117331
version: 14
---

false

**A partir das Versões:**

* 12.1.29.295
* 12.1.31.211
* 12.1.32.146
* E Superiores

# Objetivo:

---

Conforme Manual de Orientações do eSocial, para casos de ação judicial de autoria do empregador, relativa à incidência previdenciária, devem ser utilizados os códigos de incidência {codIncCP} = [95,96,97,98] e o registro {extDecisao} para determinar se a decisão judicial é somente relativa à contribuição patronal.  
  
Assim, para o objetivo deste documento é trazer informações de como gerar a tag <codIncCP> = 95 -Exclusiva do Empregador e <extDecisao> =1 (Contribuições Patronais) no evento S-1010 - Rubricas conforme layout.

---

11Execução do scriptExecução do script

Para a liberação do campo "Exclusiva do Empregador" na aba desconto será necessário atualizar sua base de dados através do aplicativo RM.Atualizador.exe.

true2ExemploExemplo

**Cadastro de Evento**

Marcado o estorno de INSS e selecionado 95 - Exclusiva do Empregador no evento de desconto.

Acessado o cadastro do Evento | Anexos | Processo de Suspensão de Incidência, selecionado a opção Contrib.Patronais do campo Extensão da Decisão/Sentença

  **XML**

**Envelope :**

**Pasta de incidências de eventos :**

**Guia de INSS**

No campo Base de INSS  foi considerado somente o evento 0002 - Dias Trabalhados  2.200,00

**Folha Analítica:**

  Base de INSS - Envelope = 2.170,00

  Base de INSS - GPS = 2.200,00

**Encargo**

## 

##
