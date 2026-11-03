---
article_id: 37721942519447
category: SIGAACD - Automação e Coleta de Dados
content_hash: 2c91028639f3bc5a6355f1e9a6c54f853a7ef95e93826406f2b61ba769ae62ed
fetched_at: '2026-06-28T22:39:13.802898+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Rastreabilidade de
  Movimentações pelo Meu Coletor de Dados
type: support-article
updated_at: '2026-01-16T12:40:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37721942519447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Rastreabilidade-de-Movimenta%C3%A7%C3%B5es-pelo-Meu-Coletor-de-Dados
---

Ao usar o aplicativo Meu Coletor de Dados para movimentações no Protheus, não há campo nativo que identifique a origem móvel. Para rastreabilidade, pode-se usar Audit Trail para registrar alterações, criar campo customizado para marcar registros ou sugerir melhoria na Central Colaborativa TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37721942513047) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Ao realizar movimentações (como transferências e baixas) através do aplicativo **Meu Coletor de Dados**, surge a necessidade de identificar, no Protheus, quais registros foram originados pelo dispositivo móvel para fins de auditoria e controle.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

Atualmente, o sistema padrão **não dispõe de um campo nativo** que sinalize a origem da movimentação especificamente como sendo do aplicativo.

Para obter essa rastreabilidade, apresentamos as alternativas abaixo:

#### **A. Auditoria via Audit Trail**

Embora não exista um log específico no ACD, é possível utilizar a ferramenta de **Framework/Configurador** chamada **Audit Trail** (Trilha de Auditoria).

* **Como funciona:** Ao implementar o Audit Trail nas tabelas dos processos de ACD (como a SD3), o sistema passa a registrar o usuário, data, hora e as alterações/exclusões realizadas.
* **Referência de Tabelas:** Para saber quais tabelas auditar conforme o processo desejado, consulte o [Guia Prático do ACD](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/1500017323122/ACD_Guia_Pratico_-_Automa__o_e_Coleta_de_Dados.pdf).
* **Configuração:** O detalhamento técnico para implementação está disponível no TDN: [Configurar Embedded Audit Trail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006847332-Framework-Linha-Protheus-Embedded-Audit-Trail).

#### 

#### **B. Criação de Campo Customizado e regras personalizadas**

É possível criar um campo de usuário na tabela **SD3 e demais.**

* **Observação:** Como o aplicativo não preenche campos customizados automaticamente, esse campo serviria para identificação via banco de dados, de acordo com as funções usadas, quando existir o acionamento de alguma rotina do ACD por exemplo ACDV120, ele sera tecnicamente preenchido com algo, assim voce tera mapeado a origem do movimento feito no App (Validar com o seu analista Desenvolvedor).

#### **C. Central Colaborativa (Sugestão de Melhoria)**

Sugerimos registrar esta necessidade como uma proposta de melhoria na [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics). Nossa equipe de Produto avalia essas demandas constantemente para futuras atualizações do padrão.

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
