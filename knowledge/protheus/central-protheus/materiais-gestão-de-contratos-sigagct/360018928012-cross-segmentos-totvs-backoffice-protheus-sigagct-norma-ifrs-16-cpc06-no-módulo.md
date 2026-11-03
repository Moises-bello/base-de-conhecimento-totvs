---
article_id: 360018928012
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d536c47448ac0db39293012ab0ef43f877dea477a89aadd3ea00b61558eea84a
fetched_at: '2026-06-28T22:37:20.081886+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Norma IFRS 16 (CPC06)
  no módulo Gestão de Contratos
type: support-article
updated_at: '2026-06-16T20:17:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018928012-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Norma-IFRS-16-CPC06-no-m%C3%B3dulo-Gest%C3%A3o-de-Contratos
---

A norma IFRS 16 (CPC06 - R2) exige que locatários reconheçam ativos e passivos para arrendamentos com prazo superior a 12 meses, refletindo o direito de uso e a obrigação de pagamento. No módulo Gestão de Contratos do Microsiga Protheus, essa norma é atendida.

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23155310186135)Tempo aproximado para leitura: 00**:10:00 min***

**Dúvida**  
Norma IFRS 16 (CPC06) no módulo Gestão de Contratos  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12.1.25  
  
  
**Solução**

### **O que é o IFRS 16 (CPC06 - R2)?**

O objetivo da **IFRS 16 (CPC06 - R2)**é relatar informações que representem fielmente as operações de arrendamento mercantil e forneça uma base para que os usuários das demonstrações contábeis avaliem o valor, o prazo e a incerteza dos fluxos de caixa decorrentes de arrendamentos. Para atender a esse objetivo, um locatário deve reconhecer ativos e passivos decorrentes de um arrendamento.

O **IFRS 16 (CPC06 - R2)** introduz um modelo contábil de locatário único e exige que o arrendatário reconheça ativos e passivos para todos os arrendamentos com prazo de mais de 12 meses, a menos que o ativo subjacente seja de baixo valor. Um arrendatário é obrigado a reconhecer um ativo de direito de uso que representa seu direito de usar o ativo arrendado subjacente e um passivo de arrendamento que representa sua obrigação de fazer pagamentos de arrendamento.

Um arrendatário mede os ativos de direito de uso de forma semelhante a outros ativos não financeiros (como imobilizado) e os passivos de arrendamento de forma similar a outros passivos financeiros. Como consequência, um arrendatário reconhece a depreciação do ativo de direito de uso e os juros sobre o passivo de arrendamento. A depreciação normalmente seria linear. Na demonstração dos fluxos de caixa, um arrendatário separa a quantia total de dinheiro pago em capital (apresentado dentro das atividades de financiamento) e juros (apresentados nas atividades operacionais ou de financiamento) de acordo com a **IAS 7**.

Ativos e passivos decorrentes de arrendamento mercantil são inicialmente mensurados com base no valor presente. A mensuração inclui pagamentos de arrendamentos não canceláveis (incluindo pagamentos indexados à inflação), e também inclui pagamentos a serem feitos em períodos opcionais se o arrendatário estiver razoavelmente certo para exercer uma opção de prolongar o arrendamento, ou não exercer a opção de rescindir o contrato de concessão. O ativo de locação inicial é igual ao passivo de locação na maioria dos casos.

O ativo de arrendamento é o direito de usar o ativo subjacente e é apresentado na demonstração da posição financeira como parte do ativo imobilizado ou como um item de linha próprio.

O **IFRS 16 (CPC06 - R2)** transporta substancialmente as exigências contábeis do arrendador no **IAS 17**. Consequentemente, um arrendador continua a classificar seus arrendamentos como arrendamentos operacionais ou arrendamentos financeiros, e a contabilizar esses dois tipos de arrendamento diferentemente.

A **IFRS 16 (CPC06 - R2)** substitui a **IAS 17**, em vigor a partir de 1 de janeiro de 2019, com a aplicação antecipada permitida. A **IFRS 16 (CPC06 - R2)**tem as seguintes disposições de transição:

* Arrendamentos financeiros existentes: continuam a ser tratados como arrendamentos financeiros.
* Locações operacionais existentes: opção para correção retrospectiva completa ou limitada para refletir os requisitos do **IFRS 16 (CPC06 - R2)**.

(Fonte: [ifrs.org](https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/#about))

### 

### **IFRS 16 (CPC06 - R2) no módulo Gestão de Contratos**

O **IFRS 16 (CPC06 - R2)** já é atendido pelo módulo de Gestão de Contratos.

Para maiores informações, acesse:

[Manutenção de Contratos - CNTA300 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=235321042)

***Obs1:***

Qual a funcionalidade do campo CNF\_AMRTZA (Amortização) contido no Cronograma Financeiro ?

Este campo tem a funcionalidade de, dentro do cálculo/funcionalidade da IFRS16, receber a informação da "Amortização Linear", conforme as informações do artigo abaixo:

[16328457 DTEXPRO-66 DT Demonstração da amortização linear](https://tdn.totvs.com/pages/viewpage.action?pageId=749071600)

***Obs2:***

O sistema possui um relatório para conferência dos valores cálculos e os valores contabilizados no IFRS16 mensalmente para a conciliação bancaria? O GCT tem algum relatório que traga as informações?

***R:*** No padrão atual do sistema, não existe funcionalidade ou relatório específico para realizar a conferência e a extração dos valores contabilizados referentes ao IFRS 16.

Os valores relacionados ao IFRS 16 ficam armazenados nas tabelas do módulo SIGAGCT, sendo:

CNF: Cronograma Financeiro;  
CNW: Cronograma Contábil.

Dessa forma, a consulta dessas informações pode ser realizada diretamente nessas tabelas, ou desenvolvidos relatórios customizados, conforme a necessidade de análise.

Caso se deseje um comportamento diferente do padrão atual, como a disponibilização de uma funcionalidade ou relatório específico para essa finalidade, orientamos a abertura de uma sugestão de melhoria por meio da Central Colaborativa, disponível no Portal do Cliente.

***Saiba Mais:***

[DMANMAT02-27582 DT Cálculo do valor presente na inclusão do contrato - IFRS16](https://tdn.totvs.com/pages/viewpage.action?pageId=555255542)

[DMANMAT02-27589 DT Cálculo do valor presente em revisões - IFRS16](https://tdn.totvs.com/pages/viewpage.action?pageId=577428003)

[DMANMAT02-30116 DT Cálculo do valor presente no Cronograma Contábil](https://tdn.totvs.com/pages/viewpage.action?pageId=578814683)

[16328457 DTEXPRO-66 DT Demonstração da amortização linear](https://tdn.totvs.com/pages/viewpage.action?pageId=749071600)

[GCT0131 - Norma IFRS 16 (CPC06)](https://tdn.totvs.com/pages/viewpage.action?pageId=430417367)

[Manutenção de Contratos - CNTA300 - Gestão de Contratos - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=235321042)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
