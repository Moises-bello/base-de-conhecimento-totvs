---
article_id: 36912210155287
category: SIGAEST - CUSTOS
content_hash: 167cf6a8413bd05ff9e2e1450c04e77d93cffe3a9b6f92079ef260c5a78822b6
fetched_at: '2026-06-28T22:39:00.591829+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Ao executar a rotina
  de Custo Médio é gerado o help "NOMOEDCTO - Não existe nenhuma moeda cadastrada"
type: support-article
updated_at: '2025-12-10T14:34:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36912210155287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Ao-executar-a-rotina-de-Custo-M%C3%A9dio-%C3%A9-gerado-o-help-NOMOEDCTO-N%C3%A3o-existe-nenhuma-moeda-cadastrada
---

O erro "NOMOEDCTO - Não existe nenhuma moeda cadastrada" ao executar a rotina de Custo Médio ocorre porque o parâmetro "Gerar Lançamento Contábil" está configurado como "Não" ou "Sim" no MATA038. Para corrigir, é necessário cadastrar uma moeda contábil no módulo 34 (Contabilidade Gerencial). Se não houver integração contábil, deve-se usar a opção "Mantém lançamento" para evitar apagar lançamentos contábeis.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36912225942935) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao executar a rotina de Custo Médio é gerado o help "**NOMOEDCTO** - Não existe nenhuma moeda cadastrada" o que fazer para corrigir?

![Captura de tela 2025-12-10 104504.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36912210143255)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Esse help é gerado porque o parametro da rotina Custo Médio e Fechamento de estoque (MATA038) o "Gerar Lançamento Contábil = Não" ou "SIM".

Para esse cenário será necessário cadastrar a moeda contábil Acessar o modulo 34 "Contabilidade Gerencial (SIGACTB)" e Incluir uma Moeda Contábil (CTBA140):

![Captura de tela 2025-12-10 104949.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36912225944343)

### **Mas eu não tenho integração com o módulo de contabilidade, o que devo fazer?**

Deve executar as rotinas envolvidas do estoque como **"Gerar Lançamento Contábil = Mantém lançamento".**

Pois caso coloque como "**Não**", conforme o próprio help do parametro informa que irá apagar os lançamentos contábeis sendo necessário ter a integração com módulo contábil.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
