---
article_id: 38601339207959
category: SIGAACD - Automação e Coleta de Dados
content_hash: b2f1c91722a5673f1afda249bc6a604f5272ce3d6297c8a5956adb18337b410b
fetched_at: '2026-06-28T22:39:13.834687+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Sugestão de quantidade
  na rotina de separação - MV_MCDSQTD
type: support-article
updated_at: '2026-02-24T12:40:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38601339207959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Sugest%C3%A3o-de-quantidade-na-rotina-de-separa%C3%A7%C3%A3o-MV-MCDSQTD
---

O artigo explica a criação do parâmetro MV\_MCDSQTD no aplicativo Meu Coletor de Dados do TOTVS Protheus, que permite sugerir automaticamente a quantidade de itens na rotina de separação. Quando habilitado, o sistema preenche a quantidade sugerida, podendo ser alterada pelo usuário. Após alterações, é necessário reiniciar o serviço REST e sincronizar os dados.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38601339186711) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Disponibilizar no **aplicativo Meu Coletor de Dados** uma opção para possibilitar que o aplicativo**sugira a quantidade do produto** na rotina de separação.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Criado o parâmetro MV\_MCDSQTDpara informar se a **quantidade** será **sugerida ou não** na rotina de **separação** dentro do **aplicativo**:

* **MV\_MCDSQTD**: Se habilitado, a quantidade será preenchida automaticamente na rotina de separação. O *default* é **desabilitado (N)**.

Quando habilitado, ao realizar uma separação, no momento de informar a quantidade do item, o sistema sugere a quantidade, permitindo que o usuário confirme ou altere a mesma. Caso o parâmetro esteja desabilitado, o sistema solicita o preenchimento da quantidade ao usuário.  
  
**Observação**

Após a criação ou alteração do parâmetro é necessário **reiniciar o serviço REST** que está provendo a comunicação com o aplicativo e também é **necessário realizar novamente o processo de sincronismo de dados.**

**![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38601339187095)      ![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38601339188247)**

---

* **DEMAIS INFORMAÇÕES**

Para utilizar esta opção na **Meu Coletor de Dados**, é necessário verificar se o parâmetro **MV\_MCDSQTD**está criado no ambiente, **seguindo a especificação abaixo:**

|  |  |
| --- | --- |
| **Parâmetro** | MV\_MCDSQTD |
| **Tipo** | Caractere |
| **Descrição** | Define se o aplicativo irá sugerir a quantidade na rotina |
| **Descrição 1** | de separação no aplicativo Meu Coletor de Dados. |
| **Descrição 2** |  |
| **Conteúdo** | (S/N) S=SIM, N=NAO |

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/pages/releaseview.action?pageId=506994322)

[Sugira a quantidade do produto na separação](https://tdn.totvs.com/pages/releaseview.action?pageId=615409037)
