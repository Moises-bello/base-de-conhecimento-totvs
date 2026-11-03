---
article_id: 360049248053
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: d18d05de594c31ba18f66c5f8ac2d870a4232febf786a74d4b5f152f8ae6486e
fetched_at: '2026-06-28T22:42:05.042078+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Documentos Fiscais
  de Entrada Não Estão Sendo Gravados Nos Blocos A, C e D da EFD Contribuições
type: support-article
updated_at: '2022-08-31T13:39:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049248053-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Documentos-Fiscais-de-Entrada-N%C3%A3o-Est%C3%A3o-Sendo-Gravados-Nos-Blocos-A-C-e-D-da-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Documentos Fiscais de Entrada Não Estão Sendo Gravados Nos **Blocos A, C e D da EFD Contribuições**  
  
**Ambiente**  
Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**  
Verificar o preenchimento do campo Atual Ativo (**F4\_ATUATF**) no cadastro de **TES** na A**ba ADM/FIN/CUSTO.**

Caso esteja com o conteúdo igual a branco será necessário avaliar junto com o setor fiscal o correto preenchimento do campo para que seja feita a correção preenchendo com o conteúdo S ou N.  
  
O sistema faz validação se o campo Atual Ativo (**F4\_ATUATF**) é diferente de N para não gerar movimento no registro de movimentação, entendendo que se trata de um ativo que irá gerar os registro **F120** ou **F130** de acordo com as configurações que são realizadas no **Ativo** para geração desses registros.  
  
Por padrão o campo no cadastro do **TES** não pode ser em branco, pois o inicializador padrão dele é "N" e se tentar alterar e deixar em branco para salvar o **TES** o sistema não irá permitir, pois o conteúdo aceito é como N ou S.

Além das informações acima, se faz necessário avaliar as configurações referente o artigo abaixo: 

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018254351-MP-FIS-EFD-CONTRIBUI%C3%87%C3%95ES-Algumas-notas-fiscais-n%C3%A3o-est%C3%A3o-sendo-levadas-para-o-arquivo-do-SPED-Contribui%C3%A7%C3%B5es-para-um-dos-blocos-A-C-e-D>
