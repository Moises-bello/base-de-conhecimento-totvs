---
article_id: 360020205231
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 43e4af33f4b8ee5d019d30cb80242a6a6d3f4bba52e9c0db5382486740b31d28
fetched_at: '2026-06-28T22:38:29.809304+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Falha na reserva do próximo
  número disponível da SD9
type: support-article
updated_at: '2025-12-30T14:33:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020205231-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Falha-na-reserva-do-pr%C3%B3ximo-n%C3%BAmero-dispon%C3%ADvel-da-SD9
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37341537738775) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**

Ao gerar a nota de saída(Mata461), o sistema está informando o help : **A461NUMNF** - **Falha na reserva do próximo número disponível da SD9 .**

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões

**Solução**

O controle de numeração por SD9 (parâmetro MV\_TPNRNFS = 3) funciona como um "Talão de Notas" digital. O sistema gera lotes de 5.000 números para consumo. A mensagem A461NUMNF ocorre quando o lote atual termina e o sistema encontra inconsistências para gerar o próximo lote de números.

![image2018-11-23_17-11-10.png](http://tdn.totvs.com/download/attachments/439353768/image2018-11-23_17-11-10.png?version=1&modificationDate=1543001121917&api=v2)  
Para resolver, siga os passos abaixo:

**1 - Ajuste de Numeração (MATA470):**

* Realize um backup da tabela SD9.
* Execute a rotina MATA470 (Ajuste de Numeração SD9). Ela excluirá registros não ocupados e reorganizará o próximo lote disponível com base no último número gravado na SF2.

**2 - Verificação de Índices:**

* A mensagem pode ocorrer por falha na leitura dos índices da SD9. Certifique-se de que a tabela possui os índices padrão conforme a imagem abaixo:

![https://totvssuporte.zendesk.com/attachments/token/riAIYagik66lf1uCgtTnRLW1J/?name=inline15779595.png](https://totvssuporte.zendesk.com/attachments/token/riAIYagik66lf1uCgtTnRLW1J/?name=inline15779595.png)

**3 - Atualização de Rotina:**

* Caso o ajuste não funcione, valide se a rotina **MATA461** está atualizada. Recomendamos aplicar o pacote acumulado do Backoffice mais recente disponível no Portal do Cliente.

**Resumo sobre o parâmetro MV\_TPNRNFS = 3:**

* **Indicação:** Recomendado para grandes volumes de faturamento para evitar *locks* (travamentos) de banco de dados.
* **Funcionamento:** Gera 5.000 registros antecipadamente na SD9.
* **Multiusuário:** Permite que várias filiais faturem simultaneamente sem conflito de numeração, especialmente se configurado com `MV_FATGCGC = .T.` (numeração por CNPJ) ou `.F.` (numeração por Filial).

**Observação:** Se você precisar pular numerações ou usar números manuais, o parâmetro `MV_MUDANUM` deve estar como `.T.`. No entanto, para o uso padrão e automatizado da SD9, recomenda-se mantê-lo como `.F.` para evitar lacunas.

**Saiba mais:**

* [Documentação Técnica: Controle de Numeração SD9](https://tdn.totvs.com/x/BBDKEg)
* [FAQ FAT0049 - Controle de Numeração de Documento de Saída](https://tdn.totvs.com/pages/viewpage.action?pageId=329024579#1-3)
* [Cross Segmentos - Backoffice Protheus - SIGAFAT - Controle de numeração da nota de saída via SD9 (MV\_TPNRNFS = 3)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019923012-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Controle-de-numera%C3%A7%C3%A3o-da-nota-de-sa%C3%ADda-via-SD9-MV-TPNRNFS-3)
