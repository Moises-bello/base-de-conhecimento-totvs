---
article_id: 7013067904919
category: esocial - Periódicos
content_hash: 18b9c291e0187e6149f536ab2d6f29d32b908c39f87143df3eb87bff7047a89c
fetched_at: '2026-06-28T22:47:09.328020+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro ao gerar XML: O campo ''matrícula'' do registro
  ''remunPerApur'' é obrigatório e não está preenchido'
type: support-article
updated_at: '2024-06-21T20:26:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7013067904919-RH-RM-FOP-eSocial-Erro-ao-gerar-XML-O-campo-matr%C3%ADcula-do-registro-remunPerApur-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24349767285143) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o XML de eventos periódicos ocorre o erro: **O campo 'matricula' do registro 'remunPerApur' é obrigatório e não está preenchido.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7012849495703)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Esse erro geralmente ocorre quando a matrícula do funcionário é obrigatória e não está preenchida no cadastro.  
  
**Solução**Para correção, é necessário executar o processo de preenchimento de matrícula para o funcionário, conforme abaixo:

1. Acesse o menu **eSocial | Saneamento de Dados | Preencher Matrícula eSocial**;  
2. Preencha os dados da tela informando a coligada e, se desejar, o filtro de funcionário;  
2.1. No caso de funcionário sem vínculo empregatício, o sistema só permitirá o preenchimento da matrícula para admissões ocorridas após a virada para o leiaute simplificado. Neste caso, basta preencher o parâmetro **Gerar matrícula para funcionário sem vínculo com admissão a partir de** com a data desejada. A data padrão informada é a da mudança da versão do leiaute para a S-1.0 e o campo não aceita data anterior a tal;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7012985797527)

3. Avance o processo até concluir sua execução.

**Importante**  
No leiaute S-1.0 o governo passou a exigir matrícula para todas as novas admissões, inclusive de funcionários sem vínculo. Assim, todas as admissões enviadas a partir de 22/05/2022 precisam ter matrícula enviada. Se a alteração do leiaute eSocial não tiver ocorrido antes dessa data no RM, é necessário alterar a data da mudança do leiaute (via banco de dados) para correta geração dos XMLs.

Tabela: PPARAMADICIONAIS | Campo: VALORSTR | Coluna: ESOCIALDATALEIAUTESIMPLIFICADO

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24349767292567)

**Saiba mais**  
Para mais informações, acesse:  
     - [Período de convivência das versões de leiaute](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5574246669207)
