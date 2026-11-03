---
article_id: 14299740690327
category: RH - Folha de Pagamento
content_hash: 8518688085c87d65b9e2f649832d03f58dc32867359148439586fd3580b12bfb
fetched_at: '2026-06-28T22:44:15.012782+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Informações referentes à Medida Provisória nº 1.171,
  de 30 de ABRIL de 2023
type: support-article
updated_at: '2025-08-11T19:42:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14299740690327-RH-Linha-Protheus-GPE-Informa%C3%A7%C3%B5es-referentes-%C3%A0-Medida-Provis%C3%B3ria-n%C2%BA-1-171-de-30-de-ABRIL-de-2023
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15272308817047) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Informações referentes à Medida Provisória nº 1.171, de 30 de ABRIL de 2023.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE Gestão de Pessoal - A partir da versão 12.1.33.  
  
**Causa**Adequações no módulo SIGAGPE para atender a Medida Provisória nº 1.171, de 30 de ABRIL de 2023.  
  
**Solução**Foi publicado no Diário Oficial da União a Medida Provisória nº 1.171, de 30 de ABRIL de 2023 que altera o cálculo de Imposto de Renda.  
  
**Pacotes liberados para as versões 12.1.33 e 12.1.2210 (necessário atualizar o dicionário).**

**Os pacotes abaixo contém as seguinte manutenções:**-Pacote inicial MP 1171/2023 - IR simplificado  
-Ajuste para que no cálculo seja respeitado o valor mínimo de IR cadastrado na Tabela S002  
-Ajuste para o sistema não considerar os ID 0215, 0216 e 0302 de previdência privada na soma do cálculo do IR simplificado   
-Ajuste no cálculo de férias partidas para não considerar o ID 0232 na soma do cálculo do IR simplificado  
-Ajuste do campo Trib. IR quando o mnemônico P\_DEDIRSIM estiver preenchido12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1123885> (garantia estendida)  
12.1.2410: <https://suporte.totvs.com/portal/p/10098/download?e=1170810>

**Consulte no *link* abaixo a documentação técnica da MP 1.1170 no SIGAGPE**[DT Cálculo do IRRF - MP](https://tdn.totvs.com/pages/viewpage.action?pageId=756458638) [1.171/2023](https://tdn.totvs.com/pages/viewpage.action?pageId=756458638)**Observações:**  
Após atualização com o pacote e dicionário da expedição contínua, pode ser necessário os procedimentos abaixo para carga das atualizações:  
-Entre em Definição tabelas pelo caminho >Atualizações >Definições cálculos >Definição Tabelas para dar carga nas novas colunas da tabela S002, após isso entre em Manutenção tabelas pelo caminho >Atualizações >Definições cálculos >Manutenção tabelas e verifique se foi atualizada (se tiver mais de uma empresa no sistema, é necessário logar primeiro na empresa para realizar o procedimento);-Entre na rotina Mnemônicos pelo caminho >Atualizações >Definições cálculos >Mnemônicos e verifique se foi criado o mnemônico P\_DEDIRSIM;  
-Entre na rotina de Verbas pelo caminho >Atualizações >Definições cálculos >Verbas e verifique se os IDs foram criados visualizando pelo campo ID p/cálculo.  
  
  
**Saiba mais**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=758481181>

[DT Cálculo do IRRF - MP](https://tdn.totvs.com/pages/viewpage.action?pageId=756458638) [1.171/2023](https://tdn.totvs.com/pages/viewpage.action?pageId=756458638)

<https://www.totvs.com/blog/fiscal-clientes/novo-calculo-de-imposto-de-renda/>
