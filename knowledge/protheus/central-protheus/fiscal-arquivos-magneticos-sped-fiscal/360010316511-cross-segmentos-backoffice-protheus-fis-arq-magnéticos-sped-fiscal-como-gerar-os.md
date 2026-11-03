---
article_id: 360010316511
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9950b3bfcaea6737e67385a1e716dd85d402186ee4d0b5e38ab597876a0595aa
fetched_at: '2026-06-28T22:42:02.209527+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar os registros 0450 e 0460?
type: support-article
updated_at: '2024-08-21T13:00:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010316511-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-os-registros-0450-e-0460
---

**Dúvida**  
Como gerar o registro **0450** e **0460** do **SPED** **FISCAL?**  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – Todas as Versões

**Solução**  
Para solucionar a dúvida acima, verifique as orientações:

1 - Gere o **Registro 0450**Tabela de Informação Complementar do documento fiscal. Neste registro são lançadas as informações complementares associadas aos documentos;

2- Cadastre na **tabela CCE** “**Informações Complementares**” o código da informação e a descrição;   
3- Realize o cadastro acessando a **Consulta Padrão (F3)** no caminho:  **Módulo Livros Fiscais**-> **Atualizações**-> **Movimentos/ Nf manual de Entrada ou Nf manual de Saída** ->**Informações Completares**;   
4- A geração do registro será realizada após o preenchimento do **campo Inf.compl (CDT\_IFCOMP)**;  
Importante: Pode ser utilizado o **Ponto de Entrada SPDPISIC** para retornar o conteúdo deste registro, junto ao **registro C110**. Para mais informações sobre esta rotina acesse: [SPDPISIC - Informações Complementares - Registro C110](http://tdn.totvs.com/pages/viewpage.action?pageId=6077215).

![image2016-6-3_22_8_18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013069592)

Importante: Complemento de nota fiscal Automático   
5 - Utilizado para **alterações automáticas** nos complementos dos documentos fiscais após a emissão das Notas Fiscais;     
6 - Para mais informações sobre o processo do **Ponto de entrada MATUCOMP**, acesse: [MATUCOMP - Alterações automáticas -- 12485;](http://tdn.totvs.com/pages/viewpage.action?pageId=6077107)7 - O parâmetro **MV\_ATUCOMP** deve ser configurado para que seja possível utilizar o **Ponto de Entrada MATUCOMP**,  **MV\_ATUCOMP = T.**

1. Gerar o **Registro 0460** Tabela de Observações do Lançamento Fiscal  
2. Neste registro serão lançadas as observações do documento fiscal provenientes de lançamentos de apuração assim como informações lançadas na coluna **Observação** na escrituração dos **Livros Fiscais de Entradas e Saídas**;  
3. Importante: Para cada documento que conter informações lançadas na coluna **Observação** dos Livros Fiscais de Entradas ou Saídas, inclua um código e uma descrição correspondente à mensagem da escrituração que será lançada na coluna **Observação** pela rotina **Informações Compl. (Tabela CCE)** e informe o código correspondente no campo do Tipo de Entrada e Saída **TES** (**Tabela SF4**) campo**Cod Observ (F4\_CODOBSE);**  
4. O código sempre será utilizado conforme cadastrado da **Tabela CCE**, porém a descrição pode variar conforme a configuração feita no cadastro do Tipo de Entrada e Saída **TES** (**Tabela SF4**) utilizado;

![image2016-6-3_22_10_43.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013077391)

5. No caso de a nota ter sido escriturada utilizando uma fórmula **(F4\_FORMULA)** amarrada ao Tipo de Entrada e Saída **TES** (**Tabela SF4**), a descrição do código utilizará o texto gravado no Livro Fiscal pela **Fórmula** **(FT\_OBSERV)**. Caso contrário, utilizará a própria descrição cadastrada na **Tabela CCE.**

**![image2016-6-3_22_10_53.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360013069812)**
