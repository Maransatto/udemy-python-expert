c = { 1,2,3,4,5 }
d = {3,3,4,4,6,7}

type(d)

uniao = c | d # {1, 2, 3, 4, 5, 6, 7}
interseccao = c & d # {3, 4}
estao_em_c_mas_nao_em_d = c - d # {1, 2, 5}
elementos_unicos = c ^ d # {1, 2, 5, 6, 7} # estão em c e d mas não estão em ambos