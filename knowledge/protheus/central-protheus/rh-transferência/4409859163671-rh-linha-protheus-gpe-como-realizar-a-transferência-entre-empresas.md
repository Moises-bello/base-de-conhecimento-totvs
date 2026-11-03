---
article_id: 4409859163671
category: RH - Transferência
content_hash: 979c04cf73ad09c46b1c29bbbd968808a41121657f6ed80adc29b53c22753c6c
fetched_at: '2026-06-28T22:43:23.328629+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a transferência entre empresas
type: support-article
updated_at: '2025-07-23T11:59:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409859163671-RH-Linha-Protheus-GPE-Como-realizar-a-transfer%C3%AAncia-entre-empresas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33657250499095) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como transferir funcionários entre empresas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No exemplo abaixo somente um funcionário será transferido e a partir do dia 01/08/2021:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409858357271)  
  
Após selecionar os funcionários, informar a data de transferência e confirmar, o sistema demonstrará a seguinte tela:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409858246167)  
  
O primeiro passo é selecionar através da lupa, qual a empresa destino para realizar a transferência. Após essa seleção, os demais campos como filial, centro de custo, devem ser preenchidos.  
  
Ao final de cada transferência, um histórico desta movimentação é gerado no **Arquivo de Transferências - SRE**.  
  
**Se a transferência for entre Empresas de raiz de CNPJ diferente (Grupo econômico)**, nessa situação o Trabalhador é demitido da Empresa origem com um motivo específico e é admitido na Empresa Destino com a Sucessão de Vínculos, porém, nessa situação pode haver a alteração da **Matricula do** **eSocial.**  
  
Quando **ambas** **Empresas** estão no mesmo ambiente do **Protheus** basta utilizar a **rotina de Transferência** do **SIGAGPE** que o Sistema cria um **evento S-2299** na Empresa origem e um evento **S-2200** na Empresa destino.  
  
Para mais informações sobre o eSocial, acesse: [RH - Linha Protheus - GPE - eSocial - S-2200 - Quando ocorre uma transferência há alteração da Matricula do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035241573-RH-Linha-Protheus-GPE-eSocial-S-2200-Quando-ocorre-uma-transfer%C3%AAncia-h%C3%A1-altera%C3%A7%C3%A3o-da-Matricula-do-eSocial)  
  
**Importante**  
Para que o **controle das transferências** seja efetuado corretamente, o**arquivo de transferências - SRE** deve estar no modo de acesso compartilhado entre filiais e também entre empresas, ou seja, deverá ser configurado na **SX2** para modo de acesso compartilhado e, além disso, se existir mais de uma empresa, o mesmo arquivo deve ser indicado.  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Movimentação de Tabelas em Transferência entre Empresas/Filiais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057237614-RH-Linha-Protheus-GPE-Movimenta%C3%A7%C3%A3o-de-Tabelas-em-Transfer%C3%AAncia-entre-Empresas-Filiais)  
[RH - Linha Protheus - GPE - Funcionamento do parâmetro MV\_ARQTRAN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013366292-RH-Linha-Protheus-GPE-Funcionamento-do-par%C3%A2metro-MV-ARQTRAN)  
[RH - Linha Protheus - GPE - Modo de compartilhamento correto para efetivação de transferência de funcionários entre empresas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060368253-RH-Linha-Protheus-GPE-Modo-de-compartilhamento-correto-para-efetiva%C3%A7%C3%A3o-de-transfer%C3%AAncia-de-funcion%C3%A1rios-entre-empresas)
