---
article_id: 32328727087767
category: PPRA / Riscos
content_hash: 8a57ac91779e54ebd9a424f1649f4dffb8447e46c349e71d3d78a65fe554d087
fetched_at: '2026-06-28T22:47:42.776159+00:00'
product: rm
section_id: 1500000834981
source: central-rm
title: 'RH - RM - SMT - PPRA/PGR - Riscos: Adequação à Portaria MTE nº 1.419 (NR-01)
  – Riscos Psicossociais'
type: support-article
updated_at: '2026-06-01T20:04:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32328727087767-RH-RM-SMT-PPRA-PGR-Riscos-Adequa%C3%A7%C3%A3o-%C3%A0-Portaria-MTE-n%C2%BA-1-419-NR-01-Riscos-Psicossociais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32328727062807) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como registrar e identificar riscos psicossociais no sistema conforme a nova Portaria MTE nº 1.419 (NR-01)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - A partir das versões **12.1.2406.279**, **12.1.2410.235**, **12.1.2502.148** e **superiores**.

**Solução**  
Conforme estabelecido pela **Portaria MTE nº 1.419**, que altera a NR-01 e passa a vigorar a partir de **26 de maio de 2025**, todas as empresas devem incorporar, em seus Programas de Gerenciamento de Riscos (PGR), a avaliação e identificação de **riscos psicossociais** no ambiente de trabalho. Essa portaria reforça a importância de considerar fatores como pressão por resultados, assédio moral, carga excessiva de trabalho, entre outros, como elementos críticos à saúde ocupacional dos trabalhadores.

🔗 Acesse a portaria completa aqui:  
[Portaria MTE nº 1.419 – NR-01 Atualizada](https://www.gov.br/trabalho-e-emprego/pt-br/acesso-a-informacao/participacao-social/conselhos-e-orgaos-colegiados/comissao-tripartite-partitaria-permanente/normas-regulamentadora/normas-regulamentadoras-vigentes/NR01atualizada2024II.pdf)

Para atender à essa adequação no sistema, foi incluída a possibilidade de marcar os riscos como psicossociais no sistema, criando-se uma flag no cadastro do **Risco,** onde quando esta flag for marcada, será possível visualizar que trata-se de um risco psicossocial através da coluna '**Psicossocial**' que foi criada na tabela **VPPRARISCOS.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32328727064471)

Essa marcação está disponível apenas para riscos cujo **Agente Agrupador** seja classificado como **Ergonômico**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32328727066775)

Recomendamos que a área de SST (Saúde e Segurança do Trabalho) revise os riscos ergonômicos já cadastrados para identificar aqueles que se enquadram como psicossociais e proceda à devida atualização. Essa prática contribuirá para o cumprimento da norma e permitirá o gerenciamento adequado dos riscos ocupacionais relacionados à saúde mental e emocional dos colaboradores.

**Importante**

Ressaltamos que os riscos psicossociais **não são enviados no evento S-2240** do eSocial, porque não conferem direito à **aposentadoria especial**. O eSocial utiliza a **Tabela 24** para identificar os agentes nocivos que podem gerar esse direito, conforme o **Anexo IV do Decreto nº 3.048/1999**. Essa tabela inclui apenas **agentes físicos**, **químicos** e **biológicos**.

Portanto, mesmo que sua empresa registre e controle os riscos psicossociais internamente, eles não são considerados para fins de aposentadoria especial e, consequentemente, não são informados no evento S-2240.  
  
Para assistir o passo a passo de como registrar e identificar riscos psicossociais, acesse o vídeo abaixo:

**Saiba Mais**

Para maiores informações, acesse:

- [Portaria MTE nº 1.419 (NR-01) – GRO – Nova Redação](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/seguranca-e-saude-no-trabalho/sst-portarias/2024/portaria-mte-no-1-419-nr-01-gro-nova-redacao.pdf)  
- [Avaliação de Riscos Psicossociais Obrigatória a partir de 2025](https://www.gov.br/trabalho-e-emprego/pt-br/noticias-e-conteudo/2024/Novembro/empresas-brasileiras-terao-que-avaliar-riscos-psicossociais-a-partir-de-2025)
