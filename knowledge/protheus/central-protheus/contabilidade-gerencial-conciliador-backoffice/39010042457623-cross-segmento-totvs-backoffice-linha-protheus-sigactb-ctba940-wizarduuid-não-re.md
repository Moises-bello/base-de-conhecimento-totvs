---
article_id: 39010042457623
category: Contabilidade Gerencial - Conciliador BackOffice
content_hash: b908d0675f67e1c0f531792be2cf4526cf3612d18ce4f4937409b2cfb2cba497
fetched_at: '2026-06-28T22:40:31.009557+00:00'
product: protheus
section_id: 31314114896791
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACTB - CTBA940 - Wizarduuid
  não realiza a criação dos campos _MSUIDT
type: support-article
updated_at: '2026-03-13T12:52:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39010042457623-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Wizarduuid-n%C3%A3o-realiza-a-cria%C3%A7%C3%A3o-dos-campos-MSUIDT
---

Durante a implantação do Conciliador Genérico (CTBA940) no Protheus, o arquivo SDF pode não criar os campos XXX\_MSUIDT se o UPDDISTR não for executado com acesso exclusivo. Para resolver, execute o compatibilizador via Wizard ou manualmente, garantindo a criação dos campos no Dicionário de Dados e a atualização do status para "Ok".

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39010020801687) Tempo aproximado para leitura: 10 min  
  
  
**Dúvida**  
Durante a implantação do Conciliador Genérico (CTBA940), ao executar a etapa de geração do arquivo SDF contendo os campos XXX\_MSUIDT via UPDDISTR, os mesmos não são criados nas respectivas tabelas, e a coluna "Situação" no assistente permanece como "Incluir", em vez de ser atualizada para "Ok".  
  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - a partir da versão 12.1.33  
  
  
**Solução**  
Este incidente ocorre porque o compatibilizador UPDDISTR não foi executado com acesso exclusivo ao sistema, o que impede a criação efetiva dos campos de identificação única (UUID).

**Passos**

1. Acesse o Wizard de Implantação do Conciliador Backoffice (WIZARDUUID) e avance até a segunda opção do Wizard (Gerar SDF)

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010042449431)
2. Verifique se os campos `XXX_MSUIDT` estão com o status "Incluir" ou "OK".

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010020802455)
3. Se estiverem como "Incluir", prossiga com a etapa para a geração do arquivo SDF para a criação dos campos.
4. Ao término da etapa, o sistema exibirá uma mensagem de "Atenção" informando que será necessário acesso exclusivo ao sistema para executar o UPDDISTR.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010042450327)
5. Selecione a opção "Sim" para rodar o compatibilizador e efetivar a criação dos campos no Dicionário de Dados (SX3).
6. Caso os campos não sejam criados rodando pela rotina, execute o UPDDISTR diretamente de forma manual.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39010042450839)
7. Retorne ao Wizard e confirme se a situação dos campos foi alterada de "Incluir" para "Ok".

**Saiba Mais**  
[CTBA940 - Conciliador BackOffice](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6451317698583-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA940-Conciliador-BackOffice)

[CTBA940 - Instalação e configuração](https://tdn.totvs.com.br/pages/releaseview.action?pageId=638741736)
