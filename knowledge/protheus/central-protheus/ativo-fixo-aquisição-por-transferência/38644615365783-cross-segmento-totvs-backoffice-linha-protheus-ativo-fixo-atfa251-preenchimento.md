---
article_id: 38644615365783
category: Ativo Fixo - Aquisição por Transferência
content_hash: 44947d946e0f6dc2780108218a5b49c57a047359efab3e25cddb33e3018ba784
fetched_at: '2026-06-28T22:41:56.959764+00:00'
product: protheus
section_id: 1500001535341
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - ATFA251 -
  Preenchimento do motivo de baixa CIAP na aquisição por transferência
type: support-article
updated_at: '2026-02-26T14:45:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38644615365783-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Ativo-Fixo-ATFA251-Preenchimento-do-motivo-de-baixa-CIAP-na-aquisi%C3%A7%C3%A3o-por-transfer%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38644562248727) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
A rotina de Aquisição por Transferência (ATFA251), após a baixa da ficha CIAP, o campo **Mot. Estorno (F9\_MOTIVO)** é preenchido como "2 - Por Venda" em situações onde não houve venda.   
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo (SIGAATF) - A partir da versão 12.1.33  
  
  
**Solução**  
O comportamento relatado é padrão do sistema. O preenchimento automático do campo **Mot. Estorno (F9\_MOTIVO)** obedece a uma regra interna amarrada ao tipo do ativo, definido no campo **Tipo Ativo (****N3\_TIPO)**.

A rotina avalia a seguinte condição para preencher o motivo do estorno:

* Quando o campo **Tipo Ativo (****N3\_TIPO)** for igual a **03 - Adiantamento**, o sistema grava automaticamente o motivo **2 - Por Venda**.
* Quando o campo **Tipo Ativo (****N3\_TIPO)** for **diferente de 03**, o sistema grava o motivo **1 - Por Perda**.

**Impacto na Geração Fiscal (EFD ICMS/IPI)** Apesar de o termo "Por Venda" causar estranheza em uma operação de transferência, é importante ressaltar que este campo **Mot. Estorno (F9\_MOTIVO)** atua apenas como uma base de transição de dados para a geração da obrigação fiscal (SPED).

O fluxo ocorre da seguinte maneira:

1. O campo **Mot. Estorno (F9\_MOTIVO)** alimenta o campo **Tipo Evento (FA\_MOTIVO)**.
2. O campo **Tipo Evento (FA\_MOTIVO)** é lido pelo sistema no momento da geração do **EFD ICMS/IPI**, especificamente para a montagem do **Registro G125** (Movimentação de Bem ou Componente do Ativo Imobilizado).
3. No Registro G125, na coluna TIPO\_MOV, o sistema traduzirá as opções gravadas. A rotina fiscal está programada para gerar a classificação **OT - Outras Saídas do Imobilizado** sempre que o campo **Tipo Evento (FA\_MOTIVO)** contiver uma das seguintes opções:

   * 2 - Por Venda;
   * 4 - Devolução;
   * 5 - Outros.

**Conclusão:** O resultado final na escrituração do **EFD ICMS/IPI** será gerado corretamente como "Outras Saídas do Imobilizado".  
  
Portanto, a seleção interna da opção "2 - Por Venda" pelo Protheus trata-se apenas de uma regra de negócio de preenchimento de tabela, não gerando nenhum impacto fiscal negativo, distorção de valores ou erro de validação para a empresa.

**Saiba Mais**  
[Criação de bem em construção(AI) para receber componentes e realizar o envio de informações para CIAP](https://tdn.totvs.com/pages/releaseview.action?pageId=567740807)  
[Como cadastrar Bem em Construção](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38509993611671-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Como-cadastrar-Bem-em-Constru%C3%A7%C3%A3o)
