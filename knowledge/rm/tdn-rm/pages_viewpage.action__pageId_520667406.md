---
content_hash: 7fd08ad52b6027368cd86538472e019bc66322eb7e6f65b530071567d8221be7
fetched_at: '2026-06-29T00:10:31.114450+00:00'
page_id: '520667406'
product: rm
source: tdn-rm
title: Como gerar a tag codIncCP com a incidência 91 e extensão da decisão/sentença(Contrib
  Patronais=1)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520667406
version: 11
---

false

**A partir das Versões:**

* 12.1.24.237
* 12.1.25.174
* 12.1.26.121

# Objetivo:

---

Conforme Manual de Orientações do eSocial, para casos de ação judicial de autoria do empregador, relativa à incidência previdenciária, devem ser utilizados os códigos de incidência {codIncCP} = [91,92,93,94] e o registro {extDecisao} para determinar se a decisão judicial é somente relativa à contribuição patronal ou se estende também à contribuição do empregado.  
  
Assim, para o objetivo deste documento é trazer informações de como gerar a tag codIncCP = 91-Mensal e extDecisao =1 (Contribuições Patronais) no evento S-1010 - Rubricas conforme layout.

---

## **Exemplo:**

**Cadastro de Evento**

 Informado no campo Exclusiva do Empregador o valor 91 - Mensal.

  

Acessando o cadastro do Evento | Anexos | Processo de Suspensão de Incidência, selecionado a opção Contrib.Patronais do campo Extensão da Decisão/Sentença

  **XML**

**Envelope :**

**Pasta de incidências de eventos**

**Guia de INSS**

No campo Base de INSS  foi considerado somente o evento 0001 -Horas normais  3.333,33

**Folha Analítica:**

  Base de INSS -Envelope =7.310,00

  Base de INSS -GPS =3.333,33
